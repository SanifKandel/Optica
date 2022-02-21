from django.conf import UserSettingsHolder
from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from register.views import registerProcess

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_register_url(self):
        url=reverse('register')
        print(url)
        self.assertEqual(resolve(url).func,registerProcess)
