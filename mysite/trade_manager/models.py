import requests
import datetime
from typing import List

from django.db import models


class Trade(models.Model):

    class Side(models.TextChoices):
        BUY = "buy"
        SELL = "sell"

    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=5)
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    total_price = models.DecimalField(max_digits=15, decimal_places=5)
    fee = models.DecimalField(max_digits=10, decimal_places=5)
    fee_coefficient = models.DecimalField(max_digits=5, decimal_places=4)
    fee_asset = models.CharField(max_length=10)
    side = models.CharField(max_length=5, choices=Side.choices)
    time_stamp = models.DateTimeField()

    @classmethod
    def get_latest_trades(cls, api_key: str) -> List[dict]:
        response = requests.get(
            "https://api.wallex.ir/v1/account/trades",
            headers = {"Content-Type": "application/json", "X-API-Key": api_key}
        )
        data = response.json()
        if response.status_code == 200:
            return data["result"]["AccountLatestTrades"]
        print(f"{data = }")

    @classmethod
    def save_latest_trades(cls, api_key: str) -> None:
        trades = cls.get_latest_trades(api_key)
        if trades is not None:
            for trade in trades:
                cls.save_trade(trade)
    
    @classmethod
    def save_trade(cls, trade: dict) -> None:
        time_stamp = cls.get_time_stamp(trade["timestamp"])
        if cls.validate_timestamp(time_stamp):
            cls.objects.create(
                symbol=trade["symbol"],
                price=trade["price"],
                quantity=trade["quantity"],
                total_price=trade["sum"],
                fee=trade["fee"],
                fee_coefficient=trade["feeCoefficient"],
                fee_asset=trade["feeAsset"],
                side=cls.get_side_from_is_buyer(trade["isBuyer"]),
                time_stamp=time_stamp
            )

    @classmethod
    def validate_timestamp(cls, time_stamp: datetime.datetime) -> bool:
        return not cls.objects.filter(time_stamp=time_stamp).exists()

    @classmethod
    def get_side_from_is_buyer(cls, is_buyer: bool) -> "side":
        if is_buyer:
            return cls.Side.BUY
        return cls.Side.SELL

    @classmethod
    def get_time_stamp(cls, timestamp: str) -> datetime.datetime:
        return datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
