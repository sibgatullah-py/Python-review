from cart import Cart
from store import Store
from cart import *

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password


# Admin Methods        
class Admin(User):
    
    
    def __init__(self,name,email):
        super().__init__(name,email,password="admin123")
        self.role = 'admin'
        
    def add_product():# done
        Store.add_product()
    
    def edit_product(product_id):
        Store.edit_product(product_id)
    
    def delete_product(product_id):
        Store.delete_product(product_id)
    
    def view_product():# done
        Store.view_product()
        
    def search_product(product_id):
        Store.search_product(product_id)



# Customer Methods        
class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.role = 'customer'
        self.cart = Cart() # cart for every customer
    
    def view_store():# done
        Store.view_product()
        
    def view_cart(self): # User will be passed in this self 
        self.cart.show_cart(self)
    
    def add_product(self):
        pass
    
    def remove_product(self):
        pass
    
    def checkout(self):
        pass
    
    def clear_cart(self):
        pass
    
  # extended  