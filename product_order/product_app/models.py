import datetime

from django.db import models

# Create your models here.


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    product_list = models.FileField(default=' ',blank=False, null=False, upload_to='myfiles/')
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)
    orders = models.ManyToManyField('Order', related_name='products', blank=True)
    price = models.IntegerField(default=0)
    ordered_quantity = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)

    def calculate_total(self):
        return self.price * self.ordered_quantity

    def save(self, *args, **kwargs):
        self.total_amount = self.calculate_total()
        super().save(*args, **kwargs)
