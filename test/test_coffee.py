import pytest
from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer
from coffee_shop.order import Order

def test_coffee_creation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    assert coffee._orders == []

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("La")

def test_coffee_orders():
    coffee = Coffee("Mocha")
    customer1 = Customer("Eve")
    customer2 = Customer("Frank")
    order1 = Order(customer1, coffee, 4.5)
    order2 = Order(customer2, coffee, 4.0)
    assert coffee.orders() == [order1, order2]

def test_coffee_customers():
    coffee = Coffee("Americano")
    customer1 = Customer("Greta")
    customer2 = Customer("Heidi")
    order1 = Order(customer1, coffee, 3.0)
    order2 = Order(customer2, coffee, 3.2)
    order3 = Order(customer1, coffee, 3.0) # Same customer again
    assert set(coffee.customers()) == {customer1, customer2}

def test_num_orders():
    coffee = Coffee("Flat White")
    customer1 = Customer("Ivy")
    customer2 = Customer("Jack")
    Order(customer1, coffee, 3.8)
    Order(customer2, coffee, 4.2)
    Order(customer1, coffee, 3.8)
    assert coffee.num_orders() == 3

def test_average_price():
    coffee = Coffee("Macchiato")
    customer1 = Customer("Kelly")
    customer2 = Customer("Liam")
    Order(customer1, coffee, 3.0)
    Order(customer2, coffee, 3.5)
    Order(customer1, coffee, 3.0)
    assert coffee.average_price() == pytest.approx((3.0 + 3.5 + 3.0) / 3)
    coffee_no_orders = Coffee("Ristretto")
    assert coffee_no_orders.average_price() == 0.0