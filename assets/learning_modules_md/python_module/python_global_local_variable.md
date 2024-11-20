## Global & Nonlocal Python Variable

Ref: https://www.geeksforgeeks.org/global-local-variables-python/

### Python Global variables:

Python Global variables are those which are not defined inside any function and have a global scope whereas Python local variables are those which are defined inside a function and their scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughout the program and inside every function.

### Python Local Variables:

Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function. Let’s see how to create a local variable.

### Why do we use Local and Global variables in Python?

Now, what if there is a Python variable with the same name initialized inside a function as well as globally? Now the question arises, will the local variable will have some effect on the global variable or vice versa, and what will happen if we change the value of a variable inside of the function f()? Will it affect the globals as well?

### Without Global and Local Variable:

#### Understand 1: Global Scope variable can be accessible inside and outside function

**Note:** As there are no locals, the value from the globals will be used but make sure both the local and the global variables should have same name.

```python
# Global scope
a = 10
print(f"outside func, a: {a}")

def func():
    print(f"inside func, a: {a}") # if a is not defined, then func can access outside global var

func()
```
outside func, a: 10 <br>
inside func, a: 10

#### Understand 2: Global Scope variable can be accessible from inside and outside function but can't be editable without defining

```python
# This function uses global variable s
def f():
    # global s  # need to specify global first to solve the error
    s += 'GFG'
    print("Inside Function", s)

# Global scope
s = "I love Geeksforgeeks"
f()
```
output: <br>
UnboundLocalError: local variable 's' referenced before assignment

#### Understand 3: Uses of "Global" Keyword

```python
a = 1

# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)
```
output:<br>
global :  1 <br>
Inside f() :  1 <br>
global :  1 <br>
Inside g() :  2 <br>
global :  1 <br>
Inside h() :  3 <br>
global :  3 <br>

#### Understand 4: Variable Scope and usage for nested child function 

```python
# Global scope
a = 10
print(f"outside func, a: {a}")

def func():
    # local variable
    a = 12
    print(f"inside func, a: {a}")
    
    def child_func():
        # without mentioning a as global, child_func can access from parent func
        print(f"inside child_func, a: {a}")
    
    child_func()
    
func()
```

outside func, a: 10 <br>
inside func, a: 12 <br>
inside child_func, a: 12 <br>

### Python Nonlocal Variables

In Python, the nonlocal keyword is used within nested functions to indicate that a variable is not local to the inner function, but rather belongs to an enclosing function’s scope. <br>
This allows you to modify a variable from the outer function within the nested function, while still keeping it distinct from global variables.

```python
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()
```
output: <br>
inner: nonlocal <br>
outer: nonlocal <br>

#### All Understandings:
1. Can't use global and nonlocal at same time
