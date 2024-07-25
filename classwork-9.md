## Module - 9: Classes and Objects

### Introduction to Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods. Objects can model real-world entities and systems, making code more modular, reusable, and easier to maintain.

### Key Concepts in OOP

1. **Classes and Objects**:
   - **Class**: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
   - **Object**: An instance of a class. Each object can have unique values for its attributes.

2. **Class Components**:
   - **Class Name**: Identifier for the class.
   - **Initialization Method (Constructor)**: `__init__(self)`, sets up the object.
   - **Member Variables (Attributes)**: Variables that store data for the object.
   - **Methods**: Functions that describe actions the object can perform.

### Example: Car Class

Let's define a `Car` class to demonstrate the concepts:

```python
class Car:
    # Class variable
    CAR_COUNT = 0

    # Constructor
    def __init__(self, make, model, color, vin, price, mpg, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.vin = vin
        self.price = price
        self.mpg = mpg
        self.year = year
        self.mileage = mileage
        self.sold = False
        self.on_lot = True
        Car.CAR_COUNT += 1

    # Method to give discount
    def give_discount(self, percentage):
        self.price -= self.price * (percentage / 100)

    # Method to increase mileage
    def increase_mileage(self, amount):
        self.mileage += amount

    # Method to sell the car
    def sell_car(self, final_price):
        self.price = final_price
        self.sold = True
        self.on_lot = False

    # Static method to get the number of cars
    @classmethod
    def get_car_count(cls):
        return cls.CAR_COUNT

# Creating objects
car1 = Car("Toyota", "Corolla", "Blue", "123ABC", 20000, 30, 2020, 15000)
car2 = Car("Honda", "Civic", "Red", "456DEF", 22000, 32, 2021, 10000)

# Using methods
car1.give_discount(10)
car1.increase_mileage(500)
car1.sell_car(18000)

# Using static method
total_cars = Car.get_car_count()
print(f"Total cars: {total_cars}")
```

### Concepts Illustrated in the Example

1. **Class and Object Creation**:
   - We defined a `Car` class and created two instances: `car1` and `car2`.

2. **Attributes and Methods**:
   - Attributes like `make`, `model`, `color` store the state of the object.
   - Methods like `give_discount`, `increase_mileage`, `sell_car` define behaviors of the object.

3. **Static Variables and Methods**:
   - `CAR_COUNT` is a class variable shared among all instances.
   - `get_car_count` is a static method that returns the total number of `Car` objects created.

### Activities

#### Activity 1: Breakout Groups: Nursery Class

Form pairs or small groups and choose a category of plant that might be sold at a plant nursery (flowers, vegetable-producing plants, shrubs, trees, etc.). Answer these questions:

- What are this plant category’s key attributes?
- What might nursery staff need to do to or with this sort of plant?

Using the `Car` class as a model, write a Python class for your chosen plant category incorporating the attributes and actions that you listed.
