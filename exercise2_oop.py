


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def __str__(self):
       return f"{self.name} price is {self.price}, and the number of quantity is {self.quantity }, total: {self.price * self.quantity}"
    


print(Product("Mustang", 50, 2))
