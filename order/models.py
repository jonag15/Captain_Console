from django.db import models
from product.models import Product
from django.contrib.auth.models import User as AuthUser
from user.models import Country


class OrderStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DeliveryType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    order_date = models.DateField()
    total_price = models.IntegerField()
    delivery = models.ForeignKey(DeliveryType, on_delete=models.PROTECT, blank=True)


class OrderedProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.product

# auth_user/user er user sem er með aðgang að kerfinu og getur skráð sig inn.
class AllUserOrders (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)


# Customer er fyrir notendur sem ekki eru skráðir inn í kerfið.
class Customer(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=999)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    mail = models.CharField(max_length=999)
    card_number = models.CharField(max_length=19)
    valid_month = models.CharField(max_length=2)
    valid_year = models.CharField(max_length=2)
    cvc = models.CharField(max_length=3)
