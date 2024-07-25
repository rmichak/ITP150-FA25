### HW-Assignment-9

#### Problem 1: Car Class with Methods
**Problem Statement:**
Create a class `Car` that has the following attributes:
- `make`
- `model`
- `year`
- `price`

The class should have the following methods:
1. `__init__` to initialize all the attributes.
2. `__str__` to return a string representation of the car in the format: "Year Make Model".
3. `apply_discount` to apply a discount to the car's price. The method should take a single parameter `discount_percentage` and reduce the car's price by that percentage.

**Example:**
```python
car = Car("Toyota", "Corolla", 2020, 20000)
print(car)  # Output: 2020 Toyota Corolla
car.apply_discount(10)
print(car.price)  # Output: 18000.0
```

#### Problem 2: Equality and Cloning
**Problem Statement:**
Create a class `Person` that has the following attributes:
- `first_name`
- `last_name`
- `age`

The class should have the following methods:
1. `__init__` to initialize all the attributes.
2. `__str__` to return a string representation of the person in the format: "First Name Last Name, Age".
3. `__eq__` to compare two `Person` objects based on their attributes.
4. `clone` to create a deep copy of the `Person` object.

**Example:**
```python
person1 = Person("John", "Doe", 30)
person2 = Person("John", "Doe", 30)
person3 = person1.clone()

print(person1 == person2)  # Output: True
print(person1 == person3)  # Output: True
print(person1 is person3)  # Output: False
```
