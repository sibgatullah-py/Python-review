from products import *
from user import *
       
        
class Store:
    def __init__(self):
        self.products = []
        
        
    def add_product(self):
        name = input("Product name: ")
        price = int(input("Product price: "))
        stock = int(input("Product stock: "))
        product = Product(name,price,stock)
        self.products.append(product)
        
    def edit_product(self,product_id):
        for product in  self.products:
            if product_id == product.id:
                name = input("Product name: ")
                price = int(input("New price: "))
                stock = int(input("New stock: "))
                
                product.name = name
                product.price = price
                product.stock += stock
                return
    
    def delete_product(self,product_id):
        for index,product in enumerate(self.products):
            if product_id == product.id:
                self.products.pop(index)
                print(f"ID {product_id} is removed")
                return
    
    def view_product(self):
        for product in self.products:
            print(f"{product.name} ---- {product.price}tk")
            
    def get_product(self,choice):
        for product in self.products:
            if choice == product.name:
                # print(f"{product.id}\n{product.name}\n{product.price}\n{product.stock}")
                return product
    
    def search_product(self,product_id):
        for product in self.products:
            if product_id == product.id:
                return product
            
        return None
        