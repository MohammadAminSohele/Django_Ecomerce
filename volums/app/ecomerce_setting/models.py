from django.db import models
import os
# Create your models here.

""" get filename ext """


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


""" upload image path """


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    finale_name = f"{instance.title}{ext}"
    return f"image-logo/{finale_name}"

""" site setting """

class SiteSetting(models.Model):
    title=models.CharField(max_length=100,verbose_name='عنوان سایت')
    address=models.CharField(max_length=100,verbose_name='ادرس')
    phone=models.CharField(max_length=100,verbose_name='تلفن')
    mobile=models.CharField(max_length=100,verbose_name='موبایل')
    fax=models.CharField(max_length=100,verbose_name='فکس')
    email=models.EmailField(max_length=100,verbose_name='ایمیل')
    about_us=models.TextField(verbose_name='درباره ما')
    copy_right=models.CharField(max_length=100,blank=True,null=True,verbose_name='متن کپی رایت')
    image=models.ImageField(verbose_name='عکس لوگو',blank=True,null=True,upload_to=upload_image_path)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='تنظیمات سایت'
        verbose_name_plural='مدیرت تنظیمات'