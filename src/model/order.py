from src.model.product import Product
from src.model.customer import Customer

class Order:

	def __init__(self, detail: list, total_price: float, loyalty_points, customer: Customer = "Customer", orderID: int = 0):
		self.detail = detail
		self.total_price = total_price 
		self.loyalty_points = int(loyalty_points)
		self.customer = customer
		self.orderID = orderID
		
	def __str__(self):

		return f" \
		Order ID: {self.orderID}\n \
		Customer: {self.customer.name} {self.customer.last_name}\n\n \
		Detail:\n\n\
		{self.detail}\n\n \
		Total: {self.total_price}\n\n \
		Loyalty points earned: {self.loyalty_points}\n"


