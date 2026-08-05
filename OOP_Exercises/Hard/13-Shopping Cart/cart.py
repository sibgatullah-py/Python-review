from user import *
from store import *

class Cart:
    def __init__(self):
        self.cart = []
        
    def add_product(self,product,quantity):
        self.cart.append({"product":product,
                          "quantity": quantity})
    
    def show_cart(self):
        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]
            price = product.price*quantity

            print(f"\nName: {product.name}")
            print(f"Quantity: {quantity}")
            print(f"Price: {price}")
            
    # methods called inside show cart logic        
    def remove_product(self,product_id):
        for product in self.cart:
            try:
                if product_id == product.id:
                    self.cart.remove(product)
                    print("Product removed")
                    break
            except StopIteration:
                print("Product does not exists")
    
    def total_price(self):
        pass
    
    def clear_cart(self):
        pass