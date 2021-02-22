class Product:
	def __init__(self, price: float, product_code: str, name: str):
		self.price = price
		self.product_code = product_code
		self.name = name

	def get_final_price(self) -> float:
		return self.price

	def get_loyalty_points(self) -> int:
		return self.price/5

	def __str__(self):
		return f" Name: {self.name}\n Price: {self.price}\n"

class Product_with_discount(Product):

	def __init__(self, price: float, product_code: str, name: str, discount: int):
		self.price = price
		self.product_code = product_code
		self.name = name
		self.discount = discount

	def get_final_price(self) -> float:
		return self.price*(1-self.discount/100)

	def get_loyalty_points(self) -> int:
		return self.price/self.discount

	def __str__(self):
		return f" Name: {self.name}\n Price: {self.price}\n Discount: {self.discount}\n"
