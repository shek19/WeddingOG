from django.contrib import admin

from .models import BudgetItem, Checklist,Guest, Vendor, Wedding, WeddingVendor

# Register your models here.
admin.site.register(Wedding)
admin.site.register(Guest)
admin.site.register(Checklist)
admin.site.register(BudgetItem)
admin.site.register(Vendor)
admin.site.register(WeddingVendor)
