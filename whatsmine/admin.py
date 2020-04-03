from django.contrib import admin
from whatsmine.models import OwnedProduct, OwnedMainline


class OwnedProductAdmin(admin.ModelAdmin):
    list_display = ('group', 'product', 'purchased_on', 'valid_until',)

admin.site.register(OwnedProduct, OwnedProductAdmin)
admin.site.register(OwnedMainline)
