## Abstract Class

```python
from abc import ABC, abstractmethod

class Car(ABC):
    
    @abstractmethod
    def car_body(self, fuel_type, no_doors, body_color):
        pass
```

### Incorrect Way
```python
class SUV_Car(Car):
    def __init__(self):
        super().__init__()
        
breeza = SUV_Car()
        
```
output: 
TypeError: Can't instantiate abstract class SUV_Car with abstract method car_body

### Correct Way

```python
class sedan_Car(Car):
    def __init__(self):
        super().__init__()
        
    def car_body(self, fuel_type=["Petrol", "diesel"], no_doors=4, body_color="white"):
        pass
        
breeza = sedan_Car()
```