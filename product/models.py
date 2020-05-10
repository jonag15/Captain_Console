from django.db import models
from user.models import User

# Create your models here.
#Þessi model hér verða möppuð inn í gagnagrunnstöflu.
#Nafnið á klasanum verður heitið á gagnagrunnstöflunni.


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

#
class ProductSubTypes(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class ProductManufacturer(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class ProductAgeLimit(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
#

class ProductStatus(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    status = models.ForeignKey(ProductStatus, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    on_sale = models.BooleanField()
    sub_type = models.ForeignKey(ProductSubTypes, on_delete=models.CASCADE)        #viðbót
    age_limit = models.ForeignKey(ProductAgeLimit, on_delete=models.CASCADE)        #viðbót
    manufacturer = models.ForeignKey(ProductManufacturer, on_delete=models.CASCADE)        #viðbót

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class SearchHistory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    search_date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)







