class Coffee:
    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string.")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")

    def __init__(self, name):
        Coffee._validate_name(name)
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        Coffee._validate_name(new_name)
        self._name = new_name

    def orders(self):
        return list(self._orders)

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0.0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

    def __repr__(self):
        return f"<Coffee(name='{self.name}')>"