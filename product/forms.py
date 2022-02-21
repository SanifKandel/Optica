from django import forms

from product.models import Products


class productfield(forms.ModelForm):

    class Meta:
        model = Products
        fields = ('name','price','brand','category','product_tags','available','image')


    