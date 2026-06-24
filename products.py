from typing import Union
from numbers import Number
class Product:
    def __init__(self, name: str, price: Number, quantity: int):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception.
        """
        if not isinstance(price, Number) or price < 0:
            raise ValueError("Price cannot be negative. Price must be a number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative. Quantity must be an integer.")
        if not isinstance(name, str) or not name:
            raise ValueError("Name cannot be empty. Name must be a string.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
    
    def get_quantity(self) -> int:
        """
        Getter function for quantity.
        Returns the quantity (int).
        """
        return self.quantity
    
    def set_quantity(self, quantity: int):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative. Quantity must be an integer.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
    
    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns whether the product is active (bool).
        """
        return self.active
    
    def activate(self):
        """
        Activates the product (sets acitve to True).
        """
        self.active = True
    
    def deactivate(self):
        """
        Deactivates the product (sets active to False).
        """
        self.active = False
    
    def show(self) -> str:
        """
        Returns a string representation of the product in the format: "name, Price: price, Quantity: quantity".
        """
        return f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"
    
    def buy(self, quantity: int) -> float:
        """
        Buys a certain quantity of the product. If the quantity is greater than the available quantity, raises an exception.
        If the purchase is successful, reduces the quantity and returns the total price (price * quantity).
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative. Quantity must be an integer.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")
        
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price

class NonStockedProduct(Product):
    """
    Non stocked products
    Some products in the store are not physical, so we don’t need to keep track of their quantity. 
    for example - a Microsoft Windows license. 
    On these products, the quantity should be set to zero and always stay that way.
    """
    def __init__(self, name: str, price: Number):
        super().__init__(name, price, quantity=0)
    
    def buy(self, quantity: int) -> float:
        """
        Buys a certain quantity of the product.
        If the purchase is successful, reduces the quantity and returns the total price (price * quantity).
        """
        total_price = self.price * quantity
        return total_price

class LimitedProduct(Product):
    """
    Limited products
    Some products can only be purchased X times in an order. 
    For example - a shipping fee can only be added once. 
    If an order is attempted with quantity larger than the maximum one, it should be refused with an exception.
    """
    def __init__(self, name: str, price: Number, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if not isinstance(maximum, int) or maximum < 0:
            raise ValueError("Quantity cannot be negative. Quantity must be an integer.")
        self.maximum = maximum
    
    def buy(self, quantity: int) -> float:
        """
        Buys a certain quantity of the product. If the quantity is greater than the maximum allowed or the available quantity, raises an exception.
        If the purchase is successful, reduces the quantity and returns the total price (price * quantity).
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative. Quantity must be an integer.")
        if quantity > self.maximum:
            raise ValueError("Quantity exeeding maximum amount. (maximum=1)")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")
        
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price

# Tests
# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

# print(bose.buy(50))
print(mac.buy(100))
print(mac.get_quantity())
print(mac.is_active())

# print(bose.show())
# print(mac.show())

# print(bose.set_quantity(1000))
# print(bose.show())
# print(mac.buy(10))
