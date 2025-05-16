# COFFEE_SHOP
# Coffee Shop Project

## Overview

This project is a Python-based implementation of a simple object-oriented model for a coffee shop. It defines the core entities of a coffee shop, including customers, coffee products, and orders, and establishes the relationships between them. This project serves as a good example of basic object-oriented design principles and Python programming.

## Features

* **Object-Oriented Design:** The project is structured around three main classes:
    * `Customer`: Represents a customer with a name and a list of orders.
    * `Coffee`: Represents a type of coffee with a name.
    * `Order`: Represents an order placed by a customer for a specific coffee at a certain price.
* **Data Validation:** The project includes input validation to ensure data integrity. For example:
    * Customer names must be strings between 1 and 15 characters long.
    * Coffee names must be strings with at least 3 characters.
    * Order prices must be numbers between 1.0 and 10.0.
* **Relationships:** The project establishes the following relationships:
    * A customer can place multiple orders.
    * Each order is for a specific coffee and is placed by a specific customer.
    * A coffee can be included in multiple orders.
* **Functionality:** The project provides the following functionalities:
    * Creating customers and coffees.
    * Placing orders for customers.
    * Retrieving a customer's orders and the coffees they have ordered.
    * Retrieving a coffee's orders and the customers who have ordered it.
    * Calculating the number of orders for a specific coffee.
    * Calculating the average price of a specific coffee.
    * Finding the customer who has spent the most on a specific coffee.
* **Testing:** The project includes a set of tests using the `pytest` framework to ensure the correctness of the implemented classes and functionalities.
* **Debugging:** The project includes a `debug.py` file for interactive testing and debugging.

## Project Structure

    coffee_shop/
    ├── coffee.py
    ├── customer.py
    ├── order.py
    ├── tests/
    │   ├── test_coffee.py
    │   ├── test_customer.py
    │   └── test_order.py
    ├── debug.py
    ├── __init__.py
    ├── Pipfile
    └── Pipfile.lock

* `coffee.py`: Contains the `Coffee` class definition.
* `customer.py`: Contains the `Customer` class definition.
* `order.py`: Contains the `Order` class definition.
* `tests/`: Contains the test files for each class.
* `debug.py`: A script for interactive testing and debugging.
* `__init__.py`: An empty file that marks the `coffee_shop` directory as a Python package.
* `Pipfile`: A file that specifies the project's dependencies using Pipenv.
* `Pipfile.lock`: A file that ensures deterministic builds by specifying the exact versions of the dependencies.

## Dependencies

The project uses the following main dependencies:

* **Pipenv:** A tool for managing dependencies and creating virtual environments.
* **pytest:** A framework for writing and running tests.

## Setup

1.  **Install Pipenv:** If you don't have Pipenv installed, you can install it using pip:

        pip install pipenv

2.  **Clone the repository:** Clone the project repository to your local machine.

        git clone <repository_url>
        cd coffee_shop

3.  **Install dependencies:** Use Pipenv to create a virtual environment and install the project's dependencies.

        pipenv install

## Usage

1.  **Activate the virtual environment:** Before running any Python code, activate the virtual environment.

        pipenv shell

2.  **Run the debug script:** To interactively test the code, run the `debug.py` script.

        python debug.py

    This will create some sample instances and demonstrate the basic functionalities. You can modify `debug.py` to test specific scenarios.

3.  **Run the tests:** To run the tests and verify the correctness of the code, use pytest.

        pytest tests/

## Classes

### `Customer`

Represents a customer.

* Attributes:
    * `name` (str): The name of the customer.
* Methods:
    * `__init__(self, name)`: Initializes a new `Customer` object.
    * `name` (property): Gets the customer's name.
    * `name` (setter): Sets the customer's name.
    * `orders(self)`: Returns a list of `Order` objects associated with the customer.
    * `coffees(self)`: Returns a list of unique `Coffee` objects the customer has ordered.
    * `create_order(self, coffee, price)`: Creates a new `Order` for the customer.
    * `most_aficionado(cls, coffee)` (class method): Finds the customer who has spent the most on a specific coffee.
    * `__repr__(self)`: Returns a string representation of the `Customer` object.

### `Coffee`

Represents a type of coffee.

* Attributes:
    * `name` (str): The name of the coffee.
* Methods:
    * `__init__(self, name)`: Initializes a new `Coffee` object.
    * `name` (property): Gets the coffee's name.
    * `name` (setter): Sets the coffee's name.
    * `orders(self)`: Returns a list of `Order` objects associated with the coffee.
    * `customers(self)`: Returns a list of unique `Customer` objects who have ordered this coffee.
    * `num_orders(self)`: Returns the number of orders for this coffee.
    * `average_price(self)`: Returns the average price of this coffee.
    * `__repr__(self)`: Returns a string representation of the `Coffee` object.

### `Order`

Represents an order placed by a customer for a specific coffee.

* Attributes:
    * `customer` (`Customer`): The customer who placed the order.
    * `coffee` (`Coffee`): The coffee ordered.
    * `price` (float): The price of the order.
* Methods:
    * `__init__(self, customer, coffee, price)`: Initializes a new `Order` object.
    * `customer` (property): Gets the customer who placed the order.
    * `coffee` (property): Gets the coffee ordered.
    * `price` (property): Gets the price of the order.
    * `price` (setter): Sets the price of the order.
    * `__repr__(self)`: Returns a string representation of the `Order` object.

## Test Suite

The project includes a comprehensive test suite using `pytest` to ensure the correctness of the code. The tests cover the following:

* Object creation and attribute validation.
* Relationship management between customers, coffees, and orders.
* Functionality of the methods in each class.
* Exception handling for invalid inputs.

To run the tests, use the following command:

    pytest tests/

## Debugging

The `debug.py` script provides a way to interactively test and debug the code. It creates sample instances of customers, coffees, and orders, and demonstrates how to use the methods to explore the relationships and functionalities. You can modify this file to test specific scenarios or debug any issues.

To run the debug script:

    python debug.py

## Further Development

This project can be extended in several ways, including:

* Adding more attributes to the classes, such as customer address, coffee description, or order date.
* Implementing more complex relationships, such as discounts, promotions, or loyalty programs.
* Adding functionality for managing the inventory of coffee beans.
* Creating a user interface (e.g., using a web framework) to interact with the coffee shop model.
* Implementing data persistence (e.g., using a database) to store and retrieve the data.

