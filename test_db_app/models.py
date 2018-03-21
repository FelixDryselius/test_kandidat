from django.db import models

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=255)
    productType = models.CharField(max_length = 255, default="give type")
    
    def __str__(self):
        return self.productName

class Batch(models.Model):
    batchNumber = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class MachineUsers(models.Model):
    userName = models.CharField(max_length=255)
    userType = models.CharField(max_length=255)