
from django.test import SimpleTestCase
from django.urls import resolve, reverse


from home.views import index


# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('index')
        print(url)
        self.assertEqual(resolve(url).func,index)