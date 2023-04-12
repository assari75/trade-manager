from django.contrib import admin
from django.urls import path

from . import models
from . import views


class TradeAdmin(admin.ModelAdmin):

    list_display = (
        "symbol",
        "price",
        "side",
        "time_stamp",
    )
    list_filter = (
        "symbol",
        "side",
    )
    change_list_template = "trade_manager/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "get-trades/",
                self.admin_site.admin_view(views.GetLatestTrades.as_view()),
                name="get-latest-trades",
            ),
        ]
        return custom_urls + urls

admin.site.register(models.Trade, TradeAdmin)
