from django.db import models
from django.contrib.auth.models import User as AuthUser


class Country(models.Model):
    name = models.CharField(max_length=255)


# auth_user/user er user sem er með aðgang að kerfinu og getur skráð sig inn.
class Address (models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=999)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Card (models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=19)
    valid_month = models.CharField(max_length=2)
    valid_year = models.CharField(max_length=2)
    cvc = models.CharField(max_length=3)


class Profile(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)


class UserImage (models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    image = models.CharField(max_length=999, default='https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/1024px-User_icon_2.svg.png')

