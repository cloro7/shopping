class Customer:

	def __init__(self, name, last_name, email: str = ''):
		self.name = name
		self.last_name = last_name
		self.email = email

	def __str__(self):
		return f" Customer: {self.last_name}, {self.name}\n"
		