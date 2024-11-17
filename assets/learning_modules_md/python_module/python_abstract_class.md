## Abstract Class -

**Abstract Class** is a class that cannot be instantiated and will contain one or more abstract methods — methods without a defined implementation.

## Abstract Method -

An **abstract method** is a method that is declared, but contains no implementation.

1. "Abstract Base Classes": Abstract Base Classes
2. Contain one or more abstract methods.
3. An abstract method is a method that is declared, but contains no implementation.
4. Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods

## Why we need to use Abstract Class and Abstract Method

1. To create a Abstract Class, we need to declare atleast one Abstract method.
2. A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.

## Below Class is not Abstract Class as it has no abstract method and we can instantiate the class

```python
class AbstractClass:
    def do_something(self):
        pass

class B(AbstractClass):
    pass

a = AbstractClass()
b = B()
```
Output:<br>
No Error

## Sample Abstract Class with 1 abstract method

```python
from abc import ABC, abstractmethod

class Car(ABC):
    
    @abstractmethod
    def car_body(self, fuel_type, no_doors, body_color):
        pass
```

## We can't instantiate a object from abstract class
```python
obj = Car()
```
output: <br>
TypeError: Can't instantiate abstract class Car with abstract method car_body

### Without defining abstract methods in subclass, will produce **error**
```python
class SUV_Car(Car):
    def __init__(self):
        super().__init__()
        
breeza = SUV_Car()
        
```
output: <br>
TypeError: Can't instantiate abstract class SUV_Car with abstract method car_body

### Correct Way to inherit Abstract Class and define the abstract mathod in subclass

```python
# Car: baseclass
# sedan_car: subclass
class sedan_Car(Car):
    def __init__(self):
        super().__init__()
        
    def car_body(self, fuel_type=["Petrol", "diesel"], no_doors=4, body_color="white"):
        pass
        
breeza = sedan_Car()
```