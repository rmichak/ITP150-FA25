## Module - 9: Classes and Objects, Methods

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

# Methods

## Table of Contents
1. **Using Methods**
    - Purpose of Methods
    - Components of a Method
    - Creating and Invoking Methods
    - Default Parameter Values
2. **Changing Default Behavior**
    - Overriding Built-in Methods
    - Dunder Methods
    - Overriding the `print` Function
    - Overriding the Equality Operator
    - Object Identity vs. Structural Equivalence
3. **Using Constructors**
    - Purpose of Constructors
    - Creating Clone Methods
4. **Getters and Setters**
    - Visibility of Variables
    - Naming Conventions for Private Variables
    - Defining Getter Methods
    - Defining Setter Methods

---

## 1. Using Methods

### 1.1 Purpose of Methods
Methods are blocks of code that perform specific actions related to an object. They help organize repetitive tasks and provide functionality to objects.

### 1.2 Components of a Method
A method has the following components:
- **Method Name**: The identifier used to refer to the method.
- **Parameter List**: Specifies the inputs for the method.
- **Method Body**: The code executed by the method.
- **Return Statement**: Specifies the value to return.

### 1.3 Creating and Invoking Methods
To create a method, define it inside a class and include `self` as the first parameter.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())
```

### 1.4 Default Parameter Values
Methods can have default parameter values.

```python
class Car:
    def __init__(self, make="Unknown", model="Unknown", year=0):
        self.make = make
        self.model = model
        self.year = year
```

---

## 2. Changing Default Behavior

### 2.1 Overriding Built-in Methods
You can override built-in methods to change their behavior for your objects.

### 2.2 Dunder Methods
Dunder methods (double underscore methods) allow customization of built-in operations.

### 2.3 Overriding the `print` Function
Override the `__str__` method to customize the string representation of an object.

```python
class Car:
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Corolla", 2020)
print(my_car)  # Outputs: 2020 Toyota Corolla
```

### 2.4 Overriding the Equality Operator
Override the `__eq__` method to compare objects based on attributes.

```python
class Car:
    def __eq__(self, other):
        return self.make == other.make and self.model == other.model and self.year == other.year
```

### 2.5 Object Identity vs. Structural Equivalence
- **Object Identity**: Whether two objects share the same memory location.
- **Structural Equivalence**: Whether two objects have the same content.

---

## 3. Using Constructors

### 3.1 Purpose of Constructors
Constructors initialize an object's properties when it's created.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
```

### 3.2 Creating Clone Methods
Clone methods create a deep copy of an object.

```python
class Car:
    def clone(self):
        return Car(self.make, self.model, self.year)

car1 = Car("Toyota", "Corolla", 2020)
car2 = car1.clone()
```

---

## 4. Getters and Setters

### 4.1 Visibility of Variables
Use single underscores to suggest private variables.

### 4.2 Naming Conventions for Private Variables
Prefix private variables with an underscore.

### 4.3 Defining Getter Methods
Getters return the value of private variables.

```python
class Car:
    def __init__(self, make, model, year):
        self._make = make

    def get_make(self):
        return self._make
```

### 4.4 Defining Setter Methods
Setters allow modification of private variables.

```python
class Car:
    def __init__(self, make):
        self._make = make

    def set_make(self, make):
        self._make = make
```
