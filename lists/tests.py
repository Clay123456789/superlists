from django.urls import resolve
from lists.views import home_page
from django.test import TestCase

class SmokeTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page) #(1)

# Create your tests here.
