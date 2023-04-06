from django.contrib import admin

from . import models


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

admin.site.register(models.Trade, TradeAdmin)
