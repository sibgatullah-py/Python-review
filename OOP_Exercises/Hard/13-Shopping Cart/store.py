from products import *
from user import *
       
        
class Store:
    products = []
        
        
    def add_product():
        name = input("Product name: ")
        price = int(input("Product price: "))
        stock = int(input("Product stock: "))
        product = Product(name,price,stock)
        Store.products.append(product)
        
    def edit_product(product_id):
        for product in  Store.products:
            if product_id == product.id:
                name = input("Product name: ")
                price = int(input("New price: "))
                stock = int(input("New stock: "))
                
                product.name = name
                product.price = price
                product.stock += stock
                return
    
    def delete_product(product_id):
        for index,product in enumerate(Store.products):
            if product_id == product.id:
                Store.products.pop(index)
                print(f"ID {product_id} is removed")
                return
    
    def view_product():
        for product in Store.products:
            print(f"{product.id} --- {product.name} --- {product.price}tk")
            
    def get_product(choice):
        for product in Store.products:
            if choice == product.name:
                # print(f"{product.id}\n{product.name}\n{product.price}\n{product.stock}")
                return product
    
    def search_product(product_id):
        for product in Store.products:
            if product_id == product.id:
                return product
            
        return None
        