from coffee import Coffee
from order import Order

class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("The customer name must be a string.")
        if not 1 <= len(name) <= 50:
            raise ValueError("The customer name must be between 1 and 50 characters long.")
        self.name = name
        self._orders = []
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("The customer name must be a string.")
        if not 1 <= len(new_name) <= 15:
            raise ValueError("The customer name must be between 1 and 15 chars long.")
        self._name = new_name

    def orders(self):
        return list(self._orders) 
    
    def coffees(self):
        return list(set(order.coffee for order in self._orders))
    
    def __repr__(self):
        return f"<Customer(name='{self.name}')>"
    
    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance.")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number.")
        if not 1.0 <= price <= 10.0:
            return ValueError("Price must be between 1.0 and 10.0.")
        order = Order(self, coffee, price)
        return order