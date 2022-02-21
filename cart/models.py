from django.db import models
from django.conf import settings

from product.models import Products

# Create your models here.

class Order(models.Model):
    user_details = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=255, default="Cash on Delivery")
    completed = models.BooleanField(default=False,null=True,blank=True)
    payment = models.BooleanField(default=False,null=True,blank=True)

    @property
    def get_orderTotal(self):
        ordereditems = self.ordereditems_set.all()
        total = sum([item.get_item_total for item in ordereditems])
        return total

    @property
    def get_TotalWith_Shipping(self):
        ordereditems = self.ordereditems_set.all()
        subtotal = sum([item.get_item_total for item in ordereditems])
        total =subtotal + 150
        return total

    @property
    def get_cart_items(self):
        ordereditems =self.ordereditems_set.all().count()
        total = ordereditems
        return total
        

    def __str__(self):
        return str(self.id)

class OrderedItems(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_item_total(self):
        item_total = self.product.price * self.quantity
        return item_total

    def __str__(self):
        return str(self.id)
