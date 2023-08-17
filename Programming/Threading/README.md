# Threading

## Process

A process is an instance of a computer program that is being executed.

Process has three basic components

- An executable program.
- The associated data needed by the program (variables, workspace, buffers, etc.)
- The execution context of the program (State of the process)

- Multiple threads can exist within one process where:
  - Each thread contains its own register set and local variables (stored in the stack).
  - All threads of a process share global variables (stored in heap) and the program code.


## Multi Threading
- Multithreading is a way of achieving multitasking.
- A **thread** is an entity within a process that can be scheduled for execution.
- Simply, a thread is a subset of a process.
- It is the smallest unit of processing that can be performed in an OS (Operating System).
### Why we need threading and when to use
- To speed up the program significantly.
- This speeding up is done by concurrently running multiple threads.
- Tasks are of two types IO Bound and CPU Bound.
- Threading is used only in case of IO Bound.
- IO Bound examples are reading/writing from files, Network operations and downloading things from Internet.
- CPU Bound examples are the tasks that actually using CPU like doing computations.
- While one thread waiting for IO Bound opearation to complete,concurrently starts the other threads instead of waiting.

### To maintain local data

create an object of local() method  then assign values to variables of that object.

```python
import threading
thread_data=threading.local()
thread_data.x=10
```

### Thread()

- It is used to create Thread.
- we have keyword arguments like name, args and target.
- name argument is used to identify the thread by name.
- target argument is used to set / target a function by using Thread.
- args is a list argument that passes the arguments to target function within [] explicitly.
- kwargs is used to pass keyword variable length arguments  to target function within {} explicitly.

```python
import threading
import time

def do_something():
    print("sleeping 1 second")
    time.sleep(1)
    print("Done Sleeping")

thread1=threading.Thread(group=None ,name="any_name",target=do_something,args=[],kwargs={}, *, daemon=None);
```

### start()

- By creating a Thread it won’t starts executing we have to invoke it using start() method.
- Start the thread’s activity. It must be called at most once per thread object.
- This method will raise a RuntimeError if called more than once on the same thread object.

```python
thread1.start()
```

### join()

- This blocks the calling current program until the thread whose join() method is called terminates.
- In simple, this allows us to execute the threads first before executing current program but after the thread execution completed.

```python
thread1.join()
```

# ThreadPool

## Resources

- Check out the [Corey Schafer](https://youtu.be/IEEhzQoKtQU) Youtube video.
- Refer [geekforgeeks](https://www.geeksforgeeks.org/multithreading-python-set-1/)
- Check out the [documentation](https://docs.python.org/3/library/threading.html#thread-objects)

[Multi Processing](Threading%20ef9aba37f4f04828854d977f2a311cf2/Multi%20Processing%20bd82b71ccb564c9ea31f0fbc6a312ff0.md)
