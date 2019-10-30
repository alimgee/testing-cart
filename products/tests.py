from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_name(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
    
    def test_price(self):
        test_price = Product(price=2.5)
        self.assertEqual(float(test_price.price), 2.5)
    
    def test_des(self):
        test_des = Product(description="2.5")
        self.assertEqual(test_des.description, '2.5')  
    
        
    def test_productpage(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)