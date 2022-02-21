from django.test import SimpleTestCase
from django.urls import resolve, reverse

from checkout.views import  checkout

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_viewcart_url(self):
        url=reverse('checkout')
        print(url)
        self.assertEqual(resolve(url).func,checkout)

