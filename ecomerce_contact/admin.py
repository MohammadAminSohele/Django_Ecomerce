from django.contrib import admin
from .models import ProductContact
# Register your models here.

class ProductContactAdmin(admin.ModelAdmin):
    list_display=['__str__','full_name','subject','is_read']
    list_filter=['is_read']
    list_editable=['is_read']
    search_fields=['subject','text']

admin.site.register(ProductContact,ProductContactAdmin)