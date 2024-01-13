from django.contrib import admin
from .models import Benefits, Blog, Display_products, Indications

# Register your models here.
class BenefitsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Benefits, BenefitsAdmin)

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Blog, BlogAdmin)

class DisplayProdsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Display_products, DisplayProdsAdmin)

class IndicationsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Indications, IndicationsAdmin)