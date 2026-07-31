from user import *
from store import *

class Cart:
    def __init__(self):
        self.cart = []
        
    def add_product(self,product):
        self.cart.append(product)
    
    def remove_product(self,product_id):
        for product in self.cart:
            try:
                if product_id == product.id:
                    self.cart.remove(product)
                    print("Product removed")
                    break
            except StopIteration:
                print("Product does not exists")
    
    def show_cart(self):
        for product in self.cart:
            print(f"{product.id }\n{product.name }\n{product.amount }\n{product.price}")
            print()
    
    def total_price(self):
        pass
    
    def clear_cart(self):
        pass