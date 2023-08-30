# All About Functions

## Functions

- A Function is a block of statements. This block of statements get executed upon calling the function.
- A function is used in case of a certain code repeating again and again, this leads to Code Repetition. To avoid this define a function with repeated statements and invoke the function when ever necessary by calling it.
- Function is defined with a keyword ***def*** and accepts arguments and also return a result.

**Types of functions:**

- **Built-in library function:** These are Standard Functions in Python that are available to use.
- **User-defined function:** We can create our own functions based on our requirements.

**Different Arguments used in functions:**

- Positional Arguments
- Keyword Arguments
- Default Arguments(arg=0)
- Variable length Arguments(*args)
- Keyword variable length Arguments(**Kwargs)

**Advantages:**

- Increases code Reusability and Code Readability.
- Avoids Code Repetition.

**Syntax:**

```python
def function_name(paramaters):
    # statements

     return expression
```

**Example:**

Write an add function that can return a sum of given arguments using Variable length arguments

```python
def add(*args):
    sum=0
    for ele in args:
        sum+=ele
    return sum

add(1,5,7,89,3,4)
```

**Output:**

```python
109
```

---

## **First Class Functions**

- A Programming language have **First Class Functions** if it treats Functions as **First Class Citizens**.
- A **First Class Citizen**(**First Class Object**) in Programming Language is an entity which supports all the operations generally available to other entities.
- These Operations include **passing function as an argument**, **assigning a function to variable** and **returning a function**(**Closures**).

### Assigning a function to a variable

```python
# Assigning function to a Variable

def square(x):
    return x*x

func_variable=square
print(func_variable(5))
```

### Passing function as an argument

```python
def square(x):
    return x*x

def cube(x):
    return x*x*x

def fun_map(func,lst):
    res=[]
    for ele in lst:
        res.append(func(ele))
    return res

lst=[1,2,3,4,5,6,7,8,9]
print(fun_map(square,lst))

print(fun_map(cube,lst))
```

### Returning a function (Closures)

```python
def html_tag(tag):
    def wrap_text(msg):
        return f"<{tag}>{msg}</{tag}>"
    return wrap_text

print_h1=html_tag("h1")
h1_header=print_h1("Hello, What going on ?")
print(h1_header)

print_p=html_tag("p")
paragraph=print_p("Example of Paragraph tag")
print(paragraph)
```

---

## **Higher Order Functions**

In Python a higher order function refers to a function that either accepts another function as an argument or returns a function as its output. This enables the utilization of functions, as values and their dynamic manipulation resulting in code that's more modular and reusable.

Python has examples of built in higher order functions such, as `map()` `filter()` and `reduce()`. These functions can be employed to apply a given function to a group of values filter out values based on a defined function and combine values using another provided function.

**Examples:**

**Closures -** Either return function as a result or takes function as an argument

---

## Lambda Functions

**Python Lambda Functions** are **anonymous function** means that the function is without a name. 

As we already know that the *def* keyword is used to define a normal function in Python. 

Similarly, the ***lambda*** keyword is used to define an anonymous function in python.

**Syntax**

**lambda** *arguments : expression*

we can pass any number of arguments to lambda functions and can have only one expression which can be evaluated and returned.

**Example-1:**

To convert a String to uppercase

```python
lambda_func=lambda x: x.upper()
print(lambda_func("Dileep"))
```

**Output:**

```
DILEEP
```

**Example-2:**

To know whether given argument is odd number or not

```python
odd_func=lambda x: x%2!=0
print(odd_func(7))
```

**Output:**

```
True
```

**Example-3:**

Lambda with if else to check max number between two numbers.

```python
Max=lambda x,y: x if x>y else y
print(Max(8,20))
```

**Output:**

```
20
```

---

## map(), filter() and reduce() functions

### map()

**map()** function applies a specified function to each item of an iterable (such as a list, tuple, or string) and then returns a new iterable containing the results.

**Example:**

```python
def square(x):
    return x*x

lst=[x for x in range(1,11)]
print("Before: ",lst)
# lst=list(map(square,lst))  # using def function
square_lst=list(map(lambda x:x*x,lst))  # using lambda function
print("After:  ",square_lst)
```

**Output:**

```python
Before:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After:   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## filter()

**filter()** function in Python filters elements from an iterable based on a given condition or function and returns a new iterable with the filtered elements.

**Example:**

```python
lst=[x for x in range(1,11)]
print("Before: ",lst)
even_list=list(filter(lambda x:x%2==0,lst))
print("After:  ",even_list)
```

**Output:**

```python
Before:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After:   [2, 4, 6, 8, 10]
```

## reduce()

**reduce()** function is used to apply a given function to the elements of an iterable in a cumulative way, reducing the iterable to a single value.

This **reduce()** function is defined in **functools** module.

**Example:**

```python
from functools import reduce
lst=[x for x in range(1,11)]
print("Before: ",lst)
even_list=list(reduce(lambda x,y:x+y,lst))
print("After:  ",even_list)
```

**Output:**

```python
Before:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After:   55
```

---

## List, Set & Dictionary Comprehension

Comprehension used to simply the task of using a for loop and iterating over a iterable to perform a simple task. It may also decreases the time and space complexity.

## List Comprehension

Produce a list of even numbers up to a given range

**Normal Way using for loop:**

```python
n=11 # range

# using for loop
lst=[]
for i in range(n):
    if i%2==0:
        lst.append(i)
print(lst)
```

**Using List Comprehension:**

```python
n=11 # range
lst1=[i for i in range(n) if i%2==0]
print(lst1)
```

**Output:**

```python
[0, 2, 4, 6, 8, 10]
```

## Dictionary Comprehension

Create a dictionary with names list item as a key and ages list item as a value.

**Normal Way using for loop:**

```python
names=["dileep","naveen","ganesh","surendra"]
ages=[22,20,17,22]

# using for loop
dict1={}
for name,age in zip(names,ages):
    dict1[name]=age
print(dict1)
```

**Using Comprehension:**

```python
names=["dileep","naveen","ganesh","surendra"]
ages=[22,20,17,22]
# using dictionary Comprehension
dict2={name:age for name,age in zip(names,ages)}
print(dict2)
```

**Output:**

```python
{'dileep': 22, 'naveen': 20, 'ganesh': 17, 'surendra': 22}
```

## Set Comprehension

Add a list of repeated elements to set

**Normal Way using for loop:**

```python
lst=[1,1,1,3,3,4,4,4,9,4,6,5,2,2]

# using for loop
set1=set()
for ele in lst:
    set1.add(ele)
print(set1)
```

**Using set Comprehension:**

```python
lst=[1,1,1,3,3,4,4,4,9,4,6,5,2,2]
# Using Set Comprehension

my_set={ele for ele in lst}
print(my_set)
```

**Output:**

```python
{1, 2, 3, 4, 5, 6, 9}
```

### **Advantages of Comprehension**

- More time-efficient and space-efficient than loops.
- Require fewer lines of code.

### **Disadvantages of Comprehension**

- Reduces readability
