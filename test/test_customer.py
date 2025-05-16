import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_customer_creation():
    customer = Customer("Alice")
    assert customer.name == "Alice"
    assert customer._orders == []

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("This name is too long")

def test_customer_orders():
    customer = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Cappuccino")
    order1 = Order(customer, coffee1, 3.5)
    order2 = Order(customer, coffee2, 4.0)
    assert customer.orders() == [order1, order2]

def test_customer_coffees():
    customer = Customer("Charlie")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Cappuccino")
    order1 = Order(customer, coffee1, 3.5)
    order2 = Order(customer, coffee2, 4.0)
    order3 = Order(customer, coffee1, 3.5) # Same coffee again
    assert set(customer.coffees()) == {coffee1, coffee2}

def test_create_order():
    customer = Customer("David")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 2.5)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 2.5
    assert order in customer.orders()
    assert order in coffee.orders()