class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        self.customer = customer
        self.cofee = coffee
        self._customer._orders.append(self)
        self._coffee._orders.append(self)
        self.price = price

    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)):
            raise TypeError("Price must be a number.")
        if not 1.0 <= new_price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = new_price
        
    def __repr__(self):
        return f"<Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})>"
    
from customer import Customer
from coffee import Coffee
