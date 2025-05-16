from coffee import Coffee
from order import Order

class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("The customer name must be a string.")
        if not 1 <= len(name) <= 50:
            raise ValueError("The customer name must be between 1 and 50 characters long.")
        if not hasattr(self.__class__, 'all_customers'):
            self.__class__.all_customers = []
        self.__class__.all_customers.append(self)
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
    
    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance.")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number.")
        if not 1.0 <= price <= 10.0:
            return ValueError("Price must be between 1.0 and 10.0.")
        order = Order(self, coffee, price)
        return order
    
    def __repr__(self):
        return f"<Customer(name='{self.name}')>"
    
    @classmethod
    def coffee_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance.")
        aficionado = None
        max_spent = 0

        if not hasattr(cls, '_all_customers'):
            cls._all_customers = []
        cls._all_customers.append(cls)

        for customer in cls._all_customers:
            total_spent = 0
            for order in customer._orders:
                if order.coffee == coffee:
                    total_spent += order.price
        
            if total_spent > max_spent:
                max_spent = total_spent
                aficionado = customer
        return aficionado
    