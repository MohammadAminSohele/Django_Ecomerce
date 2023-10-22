from django.contrib import admin

from .models import Tag

# Register your models here.

class tag_admin(admin.ModelAdmin):
    list_display=['__str__','timestamp','activate']

admin.site.register(Tag,tag_admin)