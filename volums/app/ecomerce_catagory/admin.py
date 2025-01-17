from django.contrib import admin

from .models import ProductCatagory

# Register your models here.

class catagory_admin(admin.ModelAdmin):
    list_display=['__str__','name']
    
admin.site.register(ProductCatagory,catagory_admin)