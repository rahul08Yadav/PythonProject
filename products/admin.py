from django.contrib import admin
from .models import Product, Offer
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'price', 'rating')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
