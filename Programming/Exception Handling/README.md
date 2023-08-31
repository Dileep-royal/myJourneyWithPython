# Exception Handling

Exception is a run time error that crashes our programs/ Application..

To avoid Application Crash you have to be handle them smoothly.

Python provides an in-built Class Called Exception that handles any type of exception caused during program execution.

Some of exceptions are DivisonByZeroError, ValueError, FileNotFoundError, etc.

### Keywords used in Exception Handling

- try
- except
- else
- raise
- finally

### try block

- try block contains suspicious code that causes an Exception like ZeroDivisionError, ValueError, etc.

### except block

- This block is used to handle the exception and display a user an essential information to understand. It catches the what ever exception arises in try block.
- We can have multiple except blocks. Each one for specific Exception.
- Each except block have exception name that it denotes what exception a specific except block handles.
- We can make use of built-in class Exception to handle any type of exception with a single except block. By doing so, we can accept any exception using alias and prints it.

### else block

This block code gets executed if no exception occurred in try block.

### finally block

The code in this block is executed regardless of whether an exception is raised or not.

### raise

This is used to raise an exception manually

**Two Uses:**

- To send a custom message to Exception Class to override default message.
- To send a custom arguments to Custom Exception Class.

**Example of Exception handling:**

```python
try:  
    b=10
    d=0
    e=b/d   # raises DivisionbyZeroError exception
except Exception as e:  
    print("Error: ",e)  # printing a default message of exception
else:
    print("This block excecutes whrn No Exception occured...!")
finally:
    print("executes this block whether a exception occured or not")
```

### Output

```
Error: division by zero
executes this block whether a exception occured or not
```

## Custom Exception

Custom Exceptions are user-defined exception. 

S**teps to define as Custom Exception:**

- you have to define a class with Exception Name of our own choice and also inherit parent exception class called Exception.
- If we need any attributes associated to Custom exception make sure to declare them in —init— method i.e.; constructor of the class.

**Example of custom exception:**

In the below code we defined a class called EmptyListError (Custom Exception name) with Exception class inherited.

It is used to raise an exception in case we got a empty list.

```python
class EmptyListError(Exception):
    pass

def calculate_average(numbers):
    if len(numbers) == 0:
        raise EmptyListError("Cannot calculate average of an empty list.")
# Rest of the code for calculating the average

try:
    calculate_average([])  # Passing an empty list as input
except EmptyListError as e:
    print("Error:", str(e))
```

### Custom Exception with associated arguments

- You can also add arguments to our custom path using by defining them in constructor (i.e.; “--init --” method) of custom exception class.
- Later, you can use them in except block to display detail information to user.

**Example:** Custom Exception with arguments to it

```python
class CustomException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

try:
    raise CustomException("Something went wrong.", 500)
except CustomException as e:
    print(f"Error: {e.message}")
    print(f"Error Code: {e.error_code}")
```

## Assertion in Python:

- An Assertion is a sanity check that you can turn on/off .
- Think of it like if condition is false raise an exception.

Example:

```python
def kelvinToCelsius(temp):
    assert(temp>=0), "Colder than absolute Zero"
    return (temp-273)*1.81+32
print(kelvinToCelsius(273))
print(kelvinToCelsius(-5))
```

### Output:

```python
32.0
Traceback (most recent call last):
  File "c:\Users\MSI\Desktop\Python\Exception Handling\exception.py", line 5, in <module>
    print(kelvinToCelsius(-5))
  File "c:\Users\MSI\Desktop\Python\Exception Handling\exception.py", line 2, in kelvinToCelsius
    assert(temp>=0), "Colder than absolute Zero"
AssertionError: Colder than absolute Zero
```

## Resources:

- **[Article](https://hackthedeveloper.com/python-custom-exception)** about How to create Custom Exceptions.
- You Tube [**Video**](https://youtu.be/NIWwJbo-9_8) from Corey Schafer Channel.
