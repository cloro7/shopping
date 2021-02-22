from src.model.product import Product, Product_with_discount
from src.model.customer import Customer
from src.model.order import Order
from src.model.shoppingcart import Shopping_cart

def main():
	#Instantiate products

	p1 = Product(100.0, 'product_code1', 'product_name1')
	p2 = Product(100.0, 'product_code2', 'product_name2')
	p3 = Product(100.0, 'product_code3', 'product_name3')
	p4 = Product_with_discount(100.0, 'product_code4', 'product_name4', 20)
	p5 = Product_with_discount(100.0, 'product_code5', 'product_name5', 50)


	#Populate catalogue

	product_list = [p1, p2, p3]
	Product_with_discountList = [p4, p5]
	catalogue = {}

	for product in product_list:
		key = product.product_code
		value = (product.price, product.name)
		if key not in catalogue:
			catalogue[key] = value
		else: 
			raise CatalogueError('A product with this product_code already exists.')

	for product in Product_with_discountList:
		key = product.product_code
		value = (product.price, product.name, product.discount)
		if key not in catalogue:
			catalogue[key] = value
		else: 
			raise CatalogueError('A product with this product_code already exists.')

	#Populate warehouse

	quantities = [5, 5, 5, 0, 3]
	warehouse = dict(zip(catalogue.keys(), quantities))

	#Play around with shopping cart methods 

	customer = Customer('Mandy', 'Smith')
	shopping_cart = Shopping_cart(customer = customer)

	print(shopping_cart.checkout())

	shopping_cart.add_product(p1)
	shopping_cart.add_product(p2)
	print(shopping_cart.checkout())

	shopping_cart.add_product(p3)
	print(shopping_cart.checkout())

	shopping_cart.remove_product(p2)
	print(shopping_cart.checkout())

	shopping_cart.add_promotion_code(40)
	print(shopping_cart.checkout())

if __name__ == '__main__':
	main()


#Show the catalogue to user and prompt to select products
#Review Order
#Add, remove more products
#See Catalogue
#Review Order
#Checkout
