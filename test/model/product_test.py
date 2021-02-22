import unittest

from src.model.product import Product, Product_with_discount

class Product_test(unittest.TestCase):

	def test_calculate_final_price_no_discount(self):

		product = Product(100.0, 'product_code', 'product_name')
		self.assertEqual(product.get_final_price(), 100.0)

	def test_calculate_loyalty_points_no_discount(self):
		
		product = Product(100.0, 'product_code', 'product_name')
		self.assertEqual(product.get_loyalty_points(), 20)			


	def test_should_calculate_final_price_with_discount(self):

		product = Product_with_discount(100.0, 'product_code', 'product_name', 20)
		self.assertEqual(product.get_final_price(), 80.0)

	def test_should_calculate_loyalty_points_with_discount(self):

		product = Product_with_discount(100.0, 'product_code', 'product_name', 20)
		self.assertEqual(product.get_loyalty_points(), 5)