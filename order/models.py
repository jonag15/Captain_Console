from django.db import models
from product.models import Product
from user.models import Customer
from user.models import Card

# Create your models here.


class OrderStatus(models.Model):
    name = models.CharField(max_length=255)


class DeliveryType(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    order_status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    product_quantity = models.IntegerField()
    price = models.FloatField()
    order_date = models.DateField()
    delivery = models.ForeignKey(DeliveryType, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    mail = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    card_number = models.ForeignKey(Card, on_delete=models.CASCADE)

