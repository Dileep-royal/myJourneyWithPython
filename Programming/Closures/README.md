# Closures

## Closure

A closure is a inner function that has access to variables in its outer (enclosing) scope, even after the outer function has returned. This allows for more flexible and powerful code, as functions can be used as values and manipulated dynamically.

### **Executing Both Inner and Outer Functions of a closure**

```python
def outer_fun():
    message="Hi"
    def inner_fun():
        print(message)
    return inner_fun()

outer_fun()   # executes both outer and inner functions
```

**Output:**

```
Hi
```

### **Execute only outer Function and Assign the inner function object to a variable**

```python
def outer_fun():
    message="Hi"
    def inner_fun():
        print(message)
    return inner_fun

in_fun=outer_fun()      # executes outer function and assigns the inner function object to a variable
print(in_fun.__name__)  # prints inner_fun
in_fun()                #executes inner function
```

**Output:**

```
inner_fun
Hi
```

### **Closures with Arguments**

**Example-1:**

```python
# closure with Arguments

def outer_fun(msg):
    def inner_fun():
        print(msg)
    return inner_fun

hi_fun=outer_fun("Hi")
hi_fun()     # Executing inner function with Hi message

hello_fun=outer_fun("Hello")
hello_fun()  # Executing inner function with Hello message
```

**Output:**

```python
Hi
Hello
```

**Example-2:**

```python
# Example-2

def html_tag(tag):
    def wrap_text(msg):
        return f"<{tag}>{msg}</{tag}>"
    return wrap_text

h1_tag=html_tag("h1")
p_tag=html_tag("p")

h1_tag("A header Example")
p_tag("A paragraph Example")
```

**Output:**

```
<h1>A header Example</h1>
<p>A paragraph Example</p>
```

**Example-3:**

```python
# Example-3

import logging

logging.basicConfig(filename="closure.log",level=logging.INFO)

def logger(fun):
    def log_fun(*args):
        logging.info(f"Running {fun.__name__} function with arguments {args}")
        print(fun(*args))

    return log_fun

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger=logger(add)
sub_logger=logger(sub)

add_logger(5,9)
sub_logger(40,20)
```

**Output:**

```
14
20
```

**closure.log file Contains following information**

```
INFO:root:Running add function with arguments (5, 9)
INFO:root:Running sub function with arguments (40, 20)
```