from django.test import SimpleTestCase
from django.urls import resolve, reverse

from login.views import loginProcess

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_login_url(self):
        url=reverse('login')
        print(url)
        self.assertEqual(resolve(url).func,loginProcess)