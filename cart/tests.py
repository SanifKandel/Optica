from django.test import SimpleTestCase
from django.urls import resolve, reverse

from cart.views import  contactus, viewCart, about

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_viewcart_url(self):
        url=reverse('cartIndex')
        print(url)
        self.assertEqual(resolve(url).func,viewCart)

class TestUrls(SimpleTestCase):
    def test_case_contactus_url(self):
        url=reverse('contactus')
        print(url)
        self.assertEqual(resolve(url).func,contactus)


class TestUrls(SimpleTestCase):
    def test_case_about_url(self):
        url=reverse('about')
        print(url)
        self.assertEqual(resolve(url).func,about)

