from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):
    def test_use_home_template(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
     