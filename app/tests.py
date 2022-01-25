from django.test import TestCase
from django.urls import reverse, resolve
from app.views import Registerpage,Update 

# Create your tests here.
class TestUrls(TestCase):
    def test_list_url_is_resolved(self):
        url = reverse('registerpage')
        #print(resolve(url)) ##or
        self.assertEquals(resolve(url).func,Registerpage)

    def test_list_url_resolved(self):
        
        url = reverse('update', args=["some-id"])
        #print(resolve(url)) ##or
        self.assertEquals(resolve(url).func,Update)