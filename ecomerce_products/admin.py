from django.contrib import admin

from .models import Product, ProductGallary

# Register your models here.


class productAmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'activate']


admin.site.register(Product, productAmin)
admin.site.register(ProductGallary)
