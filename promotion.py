from typing import Union
from numbers import Number
from abc import ABC, abstractmethod

class Promotion(ABC):

    def __init__(self, name: str):

        if not isinstance(name, str) or name is None:
            raise ValueError("Name cannot be empty. Name must be a string.")
        
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass
        
#Percentage discount (i.e. 20% off)
class PercentageDiscount(Promotion):
    def __init__(self, name: str, percentage: float):
        super().__init__(name)
        if not isinstance(percentage, float) or percentage < 0:
            raise ValueError("Percentage cannot be negative. Percentage must be a float.")
        self.percentage = percentage

    def apply_promotion(self, product, quantity: int) -> float:
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative. Quantity must be an integer.")
        total_no_discount = product.buy_no_promo(quantity)
        total = total_no_discount*(1-self.percentage)
        return total

#Second item at half price
class XItemHalfOff(Promotion):
    def __init__(self, name: str, x: int):
        super().__init__(name)
        if not isinstance(x, int) or x < 0:
            raise ValueError("X cannot be negative. X must be a int.")
        self.x = x

    def apply_promotion(self, product, quantity: int) -> float:
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative. Quantity must be an integer.")
        total_no_discount = product.buy_no_promo(quantity)
        reductions = quantity//self.x
        total = total_no_discount-product.get_price()*reductions*0.5
        return total

#Buy 2, get 1 free
class BuyXGetOneFree(Promotion):
    def __init__(self, name: str, x: int):
        super().__init__(name)
        if not isinstance(x, int) or x < 0:
            raise ValueError("X cannot be negative. X must be a int.")
        self.x = x

    def apply_promotion(self, product, quantity: int) -> float:
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative. Quantity must be an integer.")
        if quantity<self.x:
            total_no_discount = product.buy_no_promo(quantity)
            return total_no_discount
        elif quantity==self.x:
            print(f"Congrats, we have a {self.name} Promotion going and you get one {product.get_name()} for free.")
            total_no_discount = product.buy_no_promo(quantity)
            product.buy_no_promo(1)
            return total_no_discount
        else:
            total_no_discount = product.buy_no_promo(quantity)
            reductions = quantity//self.x
            total = total_no_discount-product.get_price()*reductions
            return total