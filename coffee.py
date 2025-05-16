class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("The coffee name must be a string.")
        if not 1 <= len(name) < 3:
            raise ValueError("The coffee name must be atleast 3 characters long.")
        self._name = name
        self.orders = []
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("The coffee name must be a string.")
        if len(new_name) < 3:
            raise ValueError("The coffee name must be atleast 3 characters long.")
        self._name = new_name

    def orders(self):
        return list(self.orders)
    
    def customers(self):
        return list(set(order.customer for order in self._orders))
    
    def __repr__(self):
        return f"<Coffee(name='{self.name}')>"
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0.0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)