from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Lead, Contact, SalesPipeline

admin.site.register(Lead)
admin.site.register(Contact)
admin.site.register(SalesPipeline)
