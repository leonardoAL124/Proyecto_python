from django.contrib import admin
from .models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Products, ProductsAdmin)
