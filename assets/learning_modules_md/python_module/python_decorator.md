## Python Decorator

**Decorator** allows programmers to modify the behaviour of a function or class. <br>
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 

### Understand Python Function as **First Class Function**:
1. A Function is an instance of the Object type.
2. function can be stored in a variable.
3. function can be passed as a parameter to another function.
4. function can be returned from a function.
5. function can be stored in data structures such as hash tables, lists

```python
def func_square(param):
    return param ** 2

def func_cube(param):
    return param ** 3
    
func_b = func_square  # assigned the function to a variable (point 2)
print(func_b(5))  # this takes the function object referenced (point 1)

def get_square_or_cube(func, param):
    print(func(param))

# function takes another function as a parameter
get_square_or_cube(func_square, 5)
get_square_or_cube(func_cube, 5)

# Returning functions from another function
def create_adder(x): 
    def adder(y): 
        return x+y 
    return adder 

add_15 = create_adder(x=15) 
print(add_15(y=10))

```

### Syntax for Decorator:

In **Decorators**, functions are taken as the argument into another function and then called inside the wrapper function

```python
@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)''' 
```

### Actual Code for Decorator:

```python
import time
from time import gmtime, strftime
import math

def calculate_duration(func):
    def inner1(*args, **kwargs):
        # storing time before function execution
        start_time = time.time()
        begin = strftime("%a, %d %b %Y %H:%M:%S", gmtime(time.time()))
        
        returned_value = func(*args, **kwargs)
        
        # storing time after function execution
        end_time = time.time()
        end = strftime("%a, %d %b %Y %H:%M:%S", gmtime(time.time()))

        seconds_elapsed = end_time - start_time
        hours, rest = divmod(seconds_elapsed, 3600)
        minutes, seconds = divmod(rest, 60)
        r_minutes = round(minutes, 2)
        r_seconds = round(seconds, 2)
        
        print(f"total time took for {func.__name__}: {begin} and {end}")
        print(f"Total execution time duration: {hours} hrs {r_minutes} mins {r_seconds} secs")
        return returned_value
    return inner1

@calculate_duration
def factorial(num):
    time.sleep(2)
    return math.factorial(num)
    
print(factorial(10))
```
output: <br>
total time took for factorial: Thu, 21 Nov 2024 17:34:20 and Thu, 21 Nov 2024 17:34:22 <br>
Total execution time duration: 0.0 hrs 0.0 mins 2.0 secs <br>
3628800 <br>

### Chaining Decorators:

```python
# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())

# The above example is similar to calling the function as –
# decor1(decor(num))
# decor(decor1(num2))
```
output: <br>
400 <br>
200 <br>