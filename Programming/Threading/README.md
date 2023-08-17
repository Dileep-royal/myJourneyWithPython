# Threading

## Process
<pre>
A process is an instance of a computer program that is being executed.

Process has three basic components

- An executable program.
- The associated data needed by the program (variables, workspace, buffers, etc.)
- The execution context of the program (State of the process)

Multiple threads can exist within one process where:
- Each thread contains its own register set and local variables (stored in the stack).
- All threads of a process share global variables (stored in heap) and the program code.
</pre>
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
- In simple, this allows us to execute the threads first before executing main thread but after the thread execution completed.

```python
thread1.join()
```
### current_thread() and main_thread()
- This functions **current_thread()** and **main_thread()** are used to get the names of current and main thread respectively.
- Thread object have **name** attribute which contains the name of the thread.
- **os.getpid()** function to get **Process ID**.
  ```python
  import threading
  import os
  print(f"Name of thread:{threading.current_thread().name}")
  print(f"Process ID:{os.getpid()}")
  ```
### Example of Threading
- In below code, we created a 10 threads, where each thread took 10 seconds to execute.
- Here, We make use of threading to speed ups the program and executed only in 1 second.

```Python
import threading
import time

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} Second(s)...')
    time.sleep(seconds)
    print(f'Done Sleeping...')
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
    
end=time.perf_counter()

print(f"Successfully Executed in {round(end-start,2)} Second(s)")
```
### Output:

```
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Done Sleeping...
Done Sleeping...
Done Sleeping...
Done Sleeping...
Done Sleeping...
Done Sleeping...
Done Sleeping...
Done Sleeping...
Done Sleeping...
Done Sleeping...
Successfully Executed in 1.02 Second(s)
```

# Python ThreadPool
**Available from Python 3.2**

- A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks. 
- The **concurrent.futures** module in Python provides a **ThreadPoolExecutor** class that makes it easy to create and manage a thread pool.

### submit() 
- **submit()** allows you to create thread and assigns a task by passing arguments for a task
- Then, expects a return value from targeted task.
- By using **result()** method we can print the return value.
```python
import concurrent.features
def do_something(seconds):
    print(f"Sleeping {seconds} Second(s)")
    time.sleep(seconds)
    return f"Done Sleeping..."

with concurrent.features.ThreadPoolExecutor() as executor:
    f1=executor.submit(do_something,1)
    print(f1.result())
```

### concurrent.features.as_completed()
- **as_completed()** method of **concurrent.features** module allows us to loop over results of threads as they completed executing.
- This is a very helpful method as it prints the thread result immediately upon on complection of execution.

### concurrent.features.map()
- **map()** method of **concurrent.features** module allows us to map target method with iteratable sequence of arguments to each thread and gives us the return value from target nethod.
- Syntax of map() method is:
```python
    concurrent.features.map(name_of_method,iterable_sequence)
```

## Real life Example of Threading
- Below code is to download images from Internet. It took a lot of time to download images one by one.
- This Downloading of images from Internet is a IO Bound task.
- This involves making a request to server to download images and it will wait to get response from server and downloads image completely.
- Instead of waiting, by using threading we can concurrently makes request to server to download other images.
- This provide us a significant speed to execute programs quickly.
  
### Code
```python
import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} is downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
```
### Output
```
photo-1516117172878-fd2c41f4a759 is downloaded...
photo-1532009324734-20a7a5813719 is downloaded...
photo-1524429656589-6633a470097c is downloaded...
photo-1530224264768-7ff8c1789d79 is downloaded...
photo-1564135624576-c5c88640f235 is downloaded...
photo-1541698444083-023c97d3f4b6 is downloaded...
photo-1522364723953-452d3431c267 is downloaded...
photo-1513938709626-033611b8cc03 is downloaded...
photo-1507143550189-fed454f93097 is downloaded...
photo-1493976040374-85c8e12f0c0e is downloaded...
photo-1504198453319-5ce911bafcde is downloaded...
photo-1530122037265-a5f1f91d3b99 is downloaded...
photo-1516972810927-80185027ca84 is downloaded...
photo-1550439062-609e1531270e is downloaded...
photo-1549692520-acc6669e2f0c is downloaded...
```

## Note
- Multithreading can help you make your programs more efficient and responsive. 
- However, it’s important to be careful when working with threads to avoid issues such as race conditions and deadlocks.

## Resources

- Check out the [Corey Schafer](https://youtu.be/IEEhzQoKtQU) Youtube video.
- Refer [geekforgeeks](https://www.geeksforgeeks.org/multithreading-python-set-1/)
- Check out the [documentation](https://docs.python.org/3/library/threading.html#thread-objects)

[Multi Processing](Threading%20ef9aba37f4f04828854d977f2a311cf2/Multi%20Processing%20bd82b71ccb564c9ea31f0fbc6a312ff0.md)
