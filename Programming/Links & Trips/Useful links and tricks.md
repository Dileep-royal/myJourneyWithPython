# Useful links and tricks

## Ternary operator

## enumerate

To iterate over both index and value

## zip

## file opening

## make use of _(underscore) instead of ,(comma) for decimal representation

while printing use formatted string to print a number by comma in terms of hundreds, thousands, lakhs... etc.

```python
num=10_000_00  # to understand clearly(readible)
print(f"{num:,}") # output is 1,000,000
```

## unpacking

## setattr() and getattr()

### setattr():

To make values of two variables as key value pair.

### getattr():

## getpass() for password input

## formatted string

<

>

^

## counter()

To count the no. of repeated elements.

## merge two sets using | (pipe)

if key of first set repeated in second set, it simply overrides it.

In below code key “b” value is overrides with 8.

Available from python 3.9

```python
x={"a":3,"b":2}
y={"b":8,"c":6}
z=x | y
print(z) # {"a":3,"b":8,"c":6}

```

## Use generators to save memory

```python
my_list=[i for i in range(10000)]
print(sum(my_list))    # 
print(sys.getsizeof(my_list,"bytes"))  # 
my_gen=(i for i in range(10000))
print(sum(my_gen))      #
print(sys.getsizeof(my_gen,"bytes"))   # 128 Bytes
```

## print list to string

use *(asterisk) to convert list to string while printing only.

[Understand the Versatility of Asterisks in Python — Know 8 Use Cases](https://betterprogramming.pub/understand-the-versatility-of-asterisks-in-python-know-8-use-cases-722bff20e84c)