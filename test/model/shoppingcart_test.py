import unittest

from src.model.shoppingcart import Shopping_cart
from src.model.product import Product, Product_with_discount
from src.model.order import Order


class Shopping_cartTest(unittest.TestCase):

	def test_should_get_products_currently_in_cart(self):

		p1 = Product(100.0, 'product_code1', 'product_name1')
		p2 = Product(100.0, 'product_code2', 'product_name2')
		product_list = [p1, p2]
		shopping_cart = Shopping_cart(product_list)

		p1_tuple = (100.0, 'product_code1', 'product_name1')
		p2_tuple = (100.0, 'product_code2', 'product_name2')
		self.assertEqual(shopping_cart.get_products(), [p1_tuple, p2_tuple])

	def test_should_add_products_to_cart(self):
		p1 = Product(100.0, 'product_code1', 'product_name1')
		p2 = Product(100.0, 'product_code2', 'product_name2')
		shopping_cart = Shopping_cart(p1)
		shopping_cart.add_product(p2)

		p1_tuple = (100.0, 'product_code1', 'product_name1')
		p2_tuple = (100.0, 'product_code2', 'product_name2')

		self.assertEqual(shopping_cart.get_products(), [p1_tuple, p2_tuple])

	def test_should_remove_products_from_cart(self):
		p1 = Product(100.0, 'product_code1', 'product_name1')
		p2 = Product(100.0, 'product_code2', 'product_name2')
		shopping_cart = Shopping_cart([p1,p2])
		shopping_cart.remove_product(p1)

		p2_tuple = (100.0, 'product_code2', 'product_name2')

		self.assertEqual(shopping_cart.get_products(), [p2_tuple])

	def test_should_add_promotion_code(self):

		shopping_cart = Shopping_cart()
		shopping_cart.add_promotion_code(10)

		self.assertEqual(shopping_cart.promotion_code, 10)

	def test_should_return_order(self):

		p1 = Product(100.0, 'product_code1', 'product_name1')
		p2 = Product(100.0, 'product_code2', 'product_name2')
		shopping_cart = Shopping_cart([p1,p2])
		
		#actually will need to mock order class...
	
		checkout = (shopping_cart.checkout())
		
		self.assertEqual(checkout.total_price, 200.0)
		self.assertEqual(checkout.loyalty_points, 40)

