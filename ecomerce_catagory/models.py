from django.db import models

# Create your models here.

class ProductCatagory(models.Model):
    title=models.CharField(max_length=120,verbose_name='عنوان')
    name=models.CharField(max_length=120,verbose_name='عنوان در url')

    class Meta:
        verbose_name='گروه'
        verbose_name_plural='گروه ها'

    def __str__(self):
        return self.title