from src.model.product import Product, Product_with_discount
from src.model.customer import Customer
from src.model.order import Order

class Shopping_cart:
	def __init__(self, products = [], customer: str = "Customer", promotion_code: int = 0):
		
		if type(products) ==list:
			self.products = products
		else:
			product_list = []
			product_list.append(products)
			self.products = product_list

		self.customer = customer
		self.promotion_code = promotion_code

	def get_products(self) -> list:
		
		product_list = []
		for product in self.products:
			product_list.append((product.price, product.product_code, product.name))

		return product_list

	def add_product(self, product, quantity = 1):
		
		self.products.append(product)

	def remove_product(self, product, quantity = 1):
		
		if product in self.products:
			self.products.remove(product)

	def add_promotion_code(self, promotion_code):
		
		self.promotion_code = promotion_code

	def checkout(self):

		total_price = sum(list(map(lambda product: product.price, self.products)))*(1-self.promotion_code/100)
		loyalty_points = sum(list(map(lambda product: product.get_loyalty_points(), self.products)))
		order = Order(self, total_price, loyalty_points, self.customer)
	
		return order

	def __str__(self):
		product_list_fmt = []
		for product in self.products:
			product_fmt = f'{product.product_code}\t{product.name}\t{product.price}\n\t\t'
			product_list_fmt.append(product_fmt)
		return ''.join(product_list_fmt)