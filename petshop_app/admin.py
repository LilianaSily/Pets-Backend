 

# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product , Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...

