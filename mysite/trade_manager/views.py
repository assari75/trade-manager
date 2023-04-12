from django import http
from django.views import generic
from django.conf import settings

from . import models


class GetLatestTrades(generic.View):
    
    def get(self, request, *args, **kwargs):
        api_key = settings.API_KEY
        models.Trade.save_latest_trades(api_key)
        return http.HttpResponseRedirect("/admin/trade_manager/trade/")
