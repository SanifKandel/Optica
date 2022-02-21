from django.test import SimpleTestCase
from django.urls import resolve, reverse

from product.views import product

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_product_url(self):
        url=reverse('productDisplay')
        print(url)
        self.assertEqual(resolve(url).func,product)