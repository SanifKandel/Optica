from django.contrib import admin
from product.models import *

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(featured)
