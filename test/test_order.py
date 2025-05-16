import pytest
from coffee_shop.order import Order
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_order_creation():
    customer = Customer("Mia")
    coffee = Coffee("Cortado")
    order = Order(customer, coffee, 3.75)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.75

def test_order_price_validation():
    customer = Customer("Noah")
    coffee = Coffee("Piccolo")
    with pytest.raises(TypeError):
        Order(customer, coffee, "expensive")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)

def test_order_customer_type_validation():
    coffee = Coffee("Long Black")
    with pytest.raises(TypeError):
        Order("Not a customer", coffee, 3.5)

def test_order_coffee_type_validation():
    customer = Customer("Olivia")
    with pytest.raises(TypeError):
        Order(customer, "Not a coffee", 4.0)