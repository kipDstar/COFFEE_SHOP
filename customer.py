from coffee import Coffee
from order import Order
from customer import Customer

class Customer:
    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters long.")

    def __init__(self, name):
        Customer._validate_name(name)
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        Customer._validate_name(new_name)
        self._name = new_name

    def orders(self):
        return list(self._orders)

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        order = Order(self, coffee, price)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        aficionado = None
        max_spent = 0
        if not hasattr(cls, '_all_customers'):
            cls._all_customers = []

        for customer in cls._all_customers:
            total_spent = 0
            for order in customer.orders():
                if order.coffee == coffee:
                    total_spent += order.price
            if total_spent > max_spent:
                max_spent = total_spent
                aficionado = customer
        return aficionado

    def __repr__(self):
        return f"<Customer(name='{self.name}')>"

    def __init__(self, name):
        Customer._validate_name(name)
        if not hasattr(self.__class__, '_all_customers'):
            self.__class__._all_customers = []
        self.__class__._all_customers.append(self)
        self._name = name
        self._orders = []