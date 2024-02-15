from django.db import models
from django.db.models import Q

import os

from ecomerce_catagory.models import ProductCatagory

# Create your models here.

""" get filename ext """


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


""" upload image path """


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    finale_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{finale_name}"


""" upload Gallary image path """


def upload_gallary_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    finale_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{finale_name}"


""" product manager """


class product_manager(models.Manager):
    def get_activate_product(self):
        return self.get_queryset().filter(activate=True)

    def get_by_id(self, productId):
        qs = self.get_queryset().filter(id=productId)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_by_catagory(self, catagory_name):
        return self.get_queryset().filter(catagories__name__iexact=catagory_name, activate=True)

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, activate=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    images = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True, verbose_name='عکس')
    activate = models.BooleanField(default=False, verbose_name='فعال/غیرفعل')
    catagories = models.ManyToManyField(
        ProductCatagory, blank=True, verbose_name='دسته بندی ها')
    visit_count = models.IntegerField(
        default=0, verbose_name='پربازدیدترین محصولات')
    about_manufacturer=models.CharField(max_length=120, verbose_name='درباره سازنده',default='لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت')    

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    object = product_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"/products/{self.id}/{self.title.replace(' ', '-')}"
        return "fsdkljfsdkljfsdkl"


class ProductGallary(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    image = models.ImageField(
        upload_to=upload_gallary_image_path, verbose_name='عکس')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='محصول')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
