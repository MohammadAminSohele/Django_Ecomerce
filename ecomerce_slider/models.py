from django.db import models

import os


""" get filename ext """
def get_filename_ext(filepath):
    basename=os.path.basename(filepath)
    name,ext=os.path.splitext(basename)
    return name,ext

""" upload image path """
def upload_image_path(instance,filename):
    name,ext=get_filename_ext(filename)
    finale_name=f"{instance.id}-{instance.title}{ext}"
    return f"slider/{finale_name}"

class Slider(models.Model):
    title=models.CharField(max_length=120,verbose_name='عنوان')
    link=models.URLField(verbose_name='ادس')
    description=models.TextField(verbose_name='توضیحات')
    image=models.ImageField(upload_to=upload_image_path,blank=True,null=True,verbose_name='عکس')

    class Meta:
        verbose_name='اسلایدر'
        verbose_name_plural='اسلایدرها'

    def __str__(self):
        return self.title