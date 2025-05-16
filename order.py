from customer import Customer
from coffee import Coffee

class Order:
    @staticmethod
    def _validate_price(price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance.")
        Order._validate_price(price)
        self._customer = customer
        self._coffee = coffee
        self._customer._orders.append(self)
        self._coffee._orders.append(self)
        self._price = price

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
        Order._validate_price(new_price)
        self._price = new_price

    def __repr__(self):
        return f"<Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})>"