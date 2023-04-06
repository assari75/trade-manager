from django.db import models


class Trade(models.Model):

    SIDE_CHOICES = [
        ("Buy", "buy"),
        ("Sell", "sell"),
    ]

    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=5)
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    total_price = models.DecimalField(max_digits=15, decimal_places=5)
    fee = models.DecimalField(max_digits=10, decimal_places=5)
    fee_coefficient = models.DecimalField(max_digits=5, decimal_places=4)
    fee_asset = models.CharField(max_length=10)
    side = models.CharField(max_length=5, choices=SIDE_CHOICES)
    time_stamp = models.DateTimeField()
