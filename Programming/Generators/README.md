# Generators

## Generators:

- A method with a **yield** keyword instead of **return** keyword is a generator .
- Method with yield keyword is a generator and gives us the **generator object** upon calling it.

Two ways to create a generator

1. A method with yield keyword instead of return.
2. By simply modifying a list comprehension by removing square brackets and instead add round brackets. (It is more looks like tuple comprehension)

Generators provides a grater performance while dealing with large amount of data like in millions.

**Advantages:**

- It will reduces the space complexity.
- generators don’t store all the values in the memory.
- Provides better performance.
- Increase readability
- decreases the no. of lines of code

### next()

- This method is used to get result of each element at a time.
- You can only use generator with **next()** method for N no. of times.
- Here N means length of list you are passing to generator method. If we call next() more than N times. It will cause a **StopIteration** Exception.

```python
Traceback (most recent call last):
  File "c:\Users\MSI\Desktop\Python\generators\generators.py", line 19, in <module>
    print(next(res))  # araises the StopIteration Exception, because exceeding the no. of iterations
StopIteration
```

### _ _*next*_ _()

- It is a special method does the same thing as next() method do.

```python
# generators
def square(lst):  # first way to create generator
    for ele in lst:
         yield ele*ele
nums=[1,2,3,4,5]
res=(i*i for i in range(1,6)) # second way to create generator
print(res)
res=square(nums)   # gives us a generator object

print(res)  # prints a generator object
print(res.__next__())   # using special method
print(res.__next__())
print(res.__next__())

print(next(res))   # normal method
print(next(res))   

print(next(res))  # araises the StopIteration Exception, because exceeding the no. of iterations
```

### Convert generator object to list

- This again the took away the benefits you get using generators.

```python
res=list(square(nums))   # gives us a list
```

## Performance check:

Modules to use to compare memory usage and time complexity:

1. time module - to know how much time took by some 
2. memory_profiler library - to know about how much memory occupied(not included in standard library)

### memory_usage()

- It is a method of memory_profiler library to measure the usage of memory.

### perf_counter()

- `Method of time module. It is used to measure the time frame between one point to other.

**This code below is to create a people list of 1M records with information like id, name and major.**

```python
import time
import memory_profiler
import random

print(f"Memory Before:{memory_profiler.memory_usage()} MB")

names=["dileep","surendra","jaswanth","ajay","mohith","jagadeesh","deena"]
majors=["CSE","EEE","ECE","MECH","CIVIL"]

def people_list(num_people):
    people=[]
    for i in range(num_people):
        person={
            "id":i,
            "name":random.choice(names),
             "major":random.choice(majors)
        }
        people.append(person)
    return people

def people_generator(num_People):
    lst=[]
    for i in range(num_People):
        person={
            "id":i,
            "name":random.choice(names),
             "major":random.choice(majors)
        }
        yield person

t1=time.perf_counter()

# data=people_list(1000000)
data=people_generator(1000000)
# people_data=list(data)       # creates a list of 1M records with people info and it again tooks time and space as "people_list" function did
t2=time.perf_counter()

print(f"Memory After:{memory_profiler.memory_usage()} MB")
print(f"Excecuted in {round(t2-t1,2)} Second(s)")
```

### Output

```python
Memory Before:[19.55078125] MB
Memory After:[289.98046875] MB
Excecuted in 0.88 Second(s)
```

### Output

```python
Memory Before:[19.45703125] MB
Memory After:[19.46875] MB
Excecuted in 0.0 Second(s)
```

## Conclusion:

<aside>
💡 It is very clear that by looking at memory usage and time took for execution while using generators almost took no time & space to create 1M records of people. This shows us that generators enhances the performance.

</aside>