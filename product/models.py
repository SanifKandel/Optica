from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class ProductBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'   

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(ProductCategory,null=True,blank=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductBrand,null=True,blank=True, on_delete=models.CASCADE)
    product_tags = models.TextField(blank=True,null=True)
    available = models.BooleanField()
    image = models.ImageField(default='default.jpg',upload_to='product_imgs',null=True,blank=True)
    
    def __str__(self):
        return f'({self.name} - {self.category})'


class featured(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'