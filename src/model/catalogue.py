from product import Product, ProductWithDiscount

class Catalogue:
	
	def __init__(self, catalogue = {}):
		self.catalogue = catalogue

	def addProduct(self, product: Product):
		if product.product_code not in self.catalogue:
			self.catalogue[product.product_code] = product
		else:
			raise Error('Duplicates: A product with the same product_code already exists in the catalogue.')

	def removeProduct(self, product: Product):
		self.catalogue.pop(product.product_code)


catalogue_single = Catalogue()
p1 = Product(10.0, "prod1", 'skjdfasljd')
p2 = Product(10.0, "prod2", 'skjdfasljd')

catalogue_single.addProduct(p1)
print(catalogue_single.catalogue)
catalogue_single.addProduct(p2)
print(catalogue_single.catalogue)
catalogue_single.removeProduct(p2)
print(catalogue_single.catalogue)