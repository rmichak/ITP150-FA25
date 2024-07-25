## Module 10: Encapsulation, Inheritance, Polymorphism

### Module: Encapsulation

#### What is Encapsulation?
Encapsulation is a fundamental concept in object-oriented programming (OOP). It involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit, known as a class. Encapsulation helps protect the internal state of an object from unintended interference and misuse.

#### Key Concepts:
1. **Instance Fields**: These are internal variables that hold data for an object. They should not be accessed directly from outside the class.
2. **Methods**: Functions that operate on instance fields. They define the behaviors of an object.
3. **Properties**: Attributes that describe an object.
4. **Self-reference**: The keyword `self` in Python refers to the current instance of the class.

#### Example:
```python
class Car:
    def __init__(self, paint_color, year):
        self._paint_color = paint_color
        self._year = year

    def get_paint_color(self):
        return self._paint_color

    def set_paint_color(self, paint_color):
        available_colors = ["Blue", "Red", "Green", "Black", "White", "Gray"]
        if paint_color in available_colors:
            self._paint_color = paint_color
        else:
            self._paint_color = "Black"

# Create an instance of Car
my_car = Car("Red", 2022)
print(my_car.get_paint_color())  # Output: Red
my_car.set_paint_color("Blue")
print(my_car.get_paint_color())  # Output: Blue
```

### Module: Inheritance

#### What is Inheritance?
Inheritance is a mechanism where a new class (child class) inherits attributes and methods from an existing class (parent class). This allows for code reusability and the creation of a hierarchical relationship between classes.

#### Key Concepts:
1. **Parent Class**: The class being inherited from.
2. **Child Class**: The class that inherits from the parent class.
3. **`super()` Function**: Used to call a method from the parent class.

#### Example:
```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")

# Create an instance of Car
my_car = Car("Toyota", "Camry", "Gasoline")
my_car.display_info()
# Output:
# Make: Toyota, Model: Camry
# Fuel Type: Gasoline
```

### Module: Polymorphism and Abstract Classes

#### What is Polymorphism?
Polymorphism allows methods to be used interchangeably between different classes. It enables a single interface to be used for different data types.

#### Key Concepts:
1. **Polymorphism**: An object can take on many forms.
2. **Virtual Methods**: Methods in a parent class that are overridden in a child class.
3. **Abstract Classes**: Classes that cannot be instantiated and are designed to be subclassed.

#### Example of Polymorphism:
```python
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

# Instantiate objects
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
```

#### Example of Abstract Classes:
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("The car engine is starting...")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("The motorcycle engine is starting...")

# Instantiate objects
car = Car()
motorcycle = Motorcycle()

car.start_engine()  # Output: The car engine is starting...
motorcycle.start_engine()  # Output: The motorcycle engine is starting...
```

### Summary
- **Encapsulation**: Bundles data and methods, protecting internal state.
- **Inheritance**: Allows for code reuse and hierarchical class relationships.
- **Polymorphism**: Enables a single interface for different data types.
- **Abstract Classes**: Provide a template for other classes to inherit from.
