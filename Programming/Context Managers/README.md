# Context Managers

Allow us to properly manage resources and what to setup and where to tear down while working with objects

### Use Case:

- File handling - automatically closes file and manages errors
- Opening and Closing connection to database
- Acquiring and releasing Lock

**Special methods associated with Context Manager while creating them using Class**

1. _ _enter_ _()
- This creates the setup for an object.
1. _ _ exit_ _()
- This method contains the things which have to be tear down.

### Context Manager designed using Class

```python
class open_file():

    def __init__(self,filename,mode) -> None:
        self.filename=filename
        self.mode=mode
        
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exc_type,exc_value,traceback):
        self.file.close()

with open_file("sample.txt","w") as f:
    f.write("Hello writing using Context Manager")

print(f.closed)
```

### Context Manager designed using decorator function

```python
# designing a Context Manger using function

from contextlib import contextmanager

@contextmanager
def open_file(filename,mode):
    try:                         # To handle exceptions
        file=open(filename,mode)
        print("function context manger")
        yield file
    finally:
        file.close()

with open_file("sample.txt","w") as f:
    f.write("Hello writing using Context Manager")

print(f.closed)
```

### **Example:**

Changing from home directory to a another directory, do some operations on that directory and get back to home directory.

**Normal Way of doing it:**

```python
# Traditional Way

import os

cwd=os.getcwd()
os.chdir("Leetcode")
print(os.listdir())
os.chdir(cwd)
print(os.getcwd())

cwd=os.getcwd()
os.chdir("Practical Python")
print(os.listdir())
os.chdir(cwd)
print(os.getcwd())
```

**Using Context Manager:**

```python
# using Context manager
import os
from contextlib import contextmanager

@contextmanager
def change_directory(directory_name):
    cwd=os.getcwd()
    os.chdir(directory_name)
    yield
    os.chdir(cwd)

with change_directory("Leetcode"):
    print(os.listdir())

with change_directory("Practical Python"):
    print(os.listdir())

print(os.getcwd())
```