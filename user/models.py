from django.db import models


# Create your models here.


class UserStatus(models.Model):
    name = models.CharField(max_length=255)


class UserRole(models.Model):
    name = models.CharField(max_length=255)


class ZipCode(models.Model):
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=255)


class Country(models.Model):
    name = models.CharField(max_length=255)


class Card(models.Model):
    card_number = models.CharField(max_length=19)
    valid_month = models.CharField(max_length=2)
    valid_year = models.CharField(max_length=2)
    cvc = models.CharField(max_length=3)


class User(models.Model):
    user_name = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    user_status = models.ForeignKey(UserStatus, on_delete=models.CASCADE)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)


class Customer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=999)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    card_number = models.ForeignKey(Card, on_delete=models.CASCADE)
    mail = models.CharField(max_length=999)


class UserImage(models.Model):
    image = models.CharField(max_length=999)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Admin(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)





