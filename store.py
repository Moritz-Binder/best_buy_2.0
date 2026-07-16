class Store:
    all_instances = []

    def __init__(self, name: str, products=None):
        self.name = name
        # Automatically register this instance upon creation
        Store.all_instances.append(self)
        
        if products is None:
            self.products = []
        else:
            self.products = products
    
    def add_product(self, product):
        """
        Adds a product to the store.
        """
        self.products.append(product)
    
    def remove_product(self, product):
        """
        Removes a product from the store if it exists.
        """
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in the store.")
        
    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity
    
    def get_all_products(self) -> list:
        """
        Returns a list of all active products in the store.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products
    
    def order(self, shopping_list) -> float:
        """
        Takes a shopping list (a dictionary of product names and quantities) and calculates the total price.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product is not None:
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Product '{product}' not found in the store.")
        return total_price

# Unit Test
# import products

# product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
#                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                 products.Product("Google Pixel 7", price=500, quantity=250),
#                ]

# best_buy = Store(product_list)
# products = best_buy.get_all_products()
# print(products)
# print(best_buy.get_total_quantity())
# print(best_buy.order([(products[0], 1), (products[1], 2)]))
