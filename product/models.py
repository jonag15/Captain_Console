from django.db import models
from user.models import Profile

# Create your models here.
#Þessi model hér verða möppuð inn í gagnagrunnstöflu.
#Nafnið á klasanum verður heitið á gagnagrunnstöflunni.


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    #product_type_slug = models.CharField(max_length=255) #Viðbót


    def __str__(self):
        return self.name



#Tengja saman type og subtype
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
    sub_type = models.ForeignKey(ProductSubTypes, on_delete=models.CASCADE)
    age_limit = models.ForeignKey(ProductAgeLimit, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(ProductManufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class SearchHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    search_date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


# Tafla fyrir öll product í subType Hasarleikir
class Hasarleikir(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



# Tafla fyrir öll product í subType Íþróttaleikir
class Itrottaleikir(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



# Tafla fyrir öll product í subType Ævintýraleikir
class Aevintyraleikir(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)