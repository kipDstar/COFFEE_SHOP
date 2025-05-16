from customer import Customer
from coffee import Coffee

# Create some instances
customer1 = Customer("Alice")
customer2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Cappuccino")

# Create some orders
order1 = customer1.create_order(coffee1, 3.5)
order2 = customer1.create_order(coffee2, 4.0)
order3 = customer2.create_order(coffee1, 3.0)

# Exploring code relationships
print(f"{customer1.name}'s orders: {customer1.orders()}")
print(f"{coffee1.name}'s orders: {coffee1.orders()}")
print(f"{coffee1.name}'s customers: {coffee1.customers()}")
print(f"{customer1.name}'s coffees: {customer1.coffees()}")

# To Test aggregate methods
print(f"Number of {coffee1.name} orders: {coffee1.num_orders()}")
print(f"Average price of {coffee1.name}: {coffee1.average_price()}")

# To Test class method
most_aficionado_latte = Customer.most_aficionado(coffee1)
if most_aficionado_latte:
    print(f"Most aficionado of {coffee1.name}: {most_aficionado_latte.name}")
else:
    print(f"No customers for {coffee1.name} yet.")



