from django.db import models
from django.contrib.auth.models import User
from ecomerce_products.models import Product
# Create your models here.

""" order model """


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='خریداری شده / نشده')
    date_paid = models.DateTimeField(
        blank=True, null=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های  خرید کاربران'

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


""" order detail model """


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت')
    count = models.IntegerField(verbose_name='تعداد')

    def get_detail_sum(self):
        return self.count * self.price

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'اطلاعات جزییات سبد خرید کاربر'
        verbose_name_plural = 'اطلاعات جزییات سبد های خرید کاربران'
