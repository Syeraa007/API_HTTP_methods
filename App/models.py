from django.db import models

# Create your models here.
class Employee(models.Model):
    Ename = models.CharField(max_length = 100)
    job = models.CharField(max_length = 100)
    sal = models.IntegerField()

    def __str__(self) -> str:
        return self.Ename

class ProductData(models.Model):
    category = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.category

class Product(models.Model):
    category = models.ForeignKey(ProductData, on_delete = models.CASCADE)
    pid = models.IntegerField(primary_key = True)
    pname = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self) -> str:
        return self.pname