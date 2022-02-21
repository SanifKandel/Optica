from django.conf import settings
from django.db import models

from datetime import datetime

from cart.models import Order

# Create your models here.

class ShippingDetails(models.Model):
    user_data = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    o_ID = models.ForeignKey(Order, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    phone = models.CharField(max_length=10,blank=True,null=True)
    email = models.CharField(max_length=150,blank=True,null=True)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=10)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def str(self):
        return self.address


