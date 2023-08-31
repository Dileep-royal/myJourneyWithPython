# Multi Processing

This Concept involves making use of Multi-Core CPU Processors.

Used to run processes asynchronously that related to CPU Bound tasks.

In multiprocessing, any newly created process will do following:

- run independently
- have their own memory space.

## Using multiprocessing module

---

In Python, the **multiprocessing** module includes a very simple and intuitive API for dividing work between multiple processes.

### Creating a Two Processes

```python
import multiprocessing
import time
import os

def do_something():
    print("Sleeping 1 Second ...")
    time.sleep(1)
    print("Done Sleeping..!") 
    print("Process ID: ",os.getpid())

if __name__=="__main__":

    start=time.perf_counter()

    p1=multiprocessing.Process(target=do_something)  # creating processes
    p2=multiprocessing.Process(target=do_something)

    

    p1.start() # To start the execution of processes
    p2.start()

    print("ID of Process P1: ",p1.pid)
    print("ID of Process P2: ",p2.pid)

    p1.join()  # join usedto complete execution of processes before executing main program.
    p2.join()

    print("Process P1 is Alive : ",p1.is_alive())
    print("Process P2 is Alive : ",p2.is_alive())
    end=time.perf_counter()

    total_time=end-start

    print(f"Finished Executing in {round(total_time,2)} Second(s)")
```

**Output:**

```python
ID of Process P1:  14092
ID of Process P2:  5600
Sleeping 1 Second ...
Sleeping 1 Second ...
Done Sleeping..!
Done Sleeping..!
Process ID:  14092
Process ID:  5600
Process P1 is Alive :  False
Process P2 is Alive :  False
Finished Executing in 1.11 Second(s)
```

### Creating a 10 Processes

```python
import multiprocessing
import time
import os

def do_something():
    print(f"Process with ID: {os.getpid()} Sleeping 1 Second...")
    
    time.sleep(1)
    print(f"Process with ID: {os.getpid()} Done Sleeping..!") 

if __name__=="__main__":

    start=time.perf_counter()
    processes=[]
    for _ in range(10):
        p=multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)
    
    for process in processes:
        process.join()
   
    end=time.perf_counter()

    total_time=end-start

    print(f"Finished Executing in {round(total_time,2)} Second(s)")
```

**Output:**

```python
Process with ID: 8560 Sleeping 1 Second...
Process with ID: 8012 Sleeping 1 Second...
Process with ID: 2036 Sleeping 1 Second...
Process with ID: 9788 Sleeping 1 Second...
Process with ID: 8060 Sleeping 1 Second...
Process with ID: 14508 Sleeping 1 Second...
Process with ID: 20160 Sleeping 1 Second...
Process with ID: 18636 Sleeping 1 Second...
Process with ID: 7424 Sleeping 1 Second...
Process with ID: 8920 Sleeping 1 Second...
Process with ID: 2036 Done Sleeping..!
Process with ID: 9788 Done Sleeping..!
Process with ID: 8012 Done Sleeping..!
Process with ID: 8560 Done Sleeping..!
Process with ID: 14508 Done Sleeping..!
Process with ID: 8060 Done Sleeping..!
Process with ID: 20160 Done Sleeping..!
Process with ID: 18636 Done Sleeping..!
Process with ID: 8920 Done Sleeping..!
Process with ID: 7424 Done Sleeping..!
Finished Executing in 1.19 Second(s)
```

### Process with arguments

```python
import multiprocessing
import time
import os

def do_something(sec):
    print(f"Process with ID: {os.getpid()} Sleeping {sec} Second(s)...")
    
    time.sleep(sec)
    print(f"Process with ID: {os.getpid()} Done Sleeping {sec} Second(s)..!")

if __name__=="__main__":

    start=time.perf_counter()
    processes=[]
    seconds=[5,4,3,2,1]
    for _ in range(10):
        p=multiprocessing.Process(target=do_something,args=([1.5]))
        p.start()
        processes.append(p)
    
    for process in processes:
        process.join()
    end=time.perf_counter()

    total_time=end-start

    print(f"Finished Executing in {round(total_time,2)} Second(s)")
```

**Output:**

```python
Process with ID: 6012 Sleeping 1.5 Second(s)...
Process with ID: 2308 Sleeping 1.5 Second(s)...
Process with ID: 17940 Sleeping 1.5 Second(s)...
Process with ID: 19936 Sleeping 1.5 Second(s)...
Process with ID: 21304 Sleeping 1.5 Second(s)...
Process with ID: 13596 Sleeping 1.5 Second(s)...
Process with ID: 4936 Sleeping 1.5 Second(s)...
Process with ID: 2604 Sleeping 1.5 Second(s)...
Process with ID: 15976 Sleeping 1.5 Second(s)...
Process with ID: 2664 Sleeping 1.5 Second(s)...
Process with ID: 6012 Done Sleeping 1.5 Second(s)..!
Process with ID: 2308 Done Sleeping 1.5 Second(s)..!
Process with ID: 17940 Done Sleeping 1.5 Second(s)..!
Process with ID: 19936 Done Sleeping 1.5 Second(s)..!
Process with ID: 21304 Done Sleeping 1.5 Second(s)..!
Process with ID: 2604 Done Sleeping 1.5 Second(s)..!
Process with ID: 4936 Done Sleeping 1.5 Second(s)..!
Process with ID: 13596 Done Sleeping 1.5 Second(s)..!
Process with ID: 2664 Done Sleeping 1.5 Second(s)..!
Process with ID: 15976 Done Sleeping 1.5 Second(s)..!
Finished Executing in 1.72 Second(s)
```

---

## Process Pool from Concurrent.futures module

---

### submit() method

```python
import concurrent.futures
import time
import os

def do_something():
    print(f"Process with ID: {os.getpid()} Sleeping 1 Second...")
    time.sleep(1)
    return f"Process with ID: {os.getpid()} Done Sleeping..!"

result=[]

if __name__=="__main__":

    start=time.perf_counter()
    processes=[]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1=executor.submit(do_something)
        print(f1.result())  # print return result from target method.

    end=time.perf_counter()

    total_time=end-start

    print(f"Finished Executing in {round(total_time,2)} Second(s)")
```

**Output:**

```python
Process with ID: 2156 Sleeping 1 Second...
Process with ID: 2156 Done Sleeping..!
Finished Executing in 1.13 Second(s)
```

### as_completed() method

- Prints the result immediately after a execution of process completed.

```python
import concurrent.futures
import time
import os

def do_something(sec):
    print(f"Process with ID: {os.getpid()} Sleeping {sec} Second(s)...")
    
    time.sleep(sec)
    return f"Process with ID: {os.getpid()} Done Sleeping {sec} Second(s)..!"

result=[]

if __name__=="__main__":

    start=time.perf_counter()
    processes=[]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds=[5,4,3,2,1]
        results=[executor.submit(do_something,sec) for sec in seconds]

        for f in concurrent.futures.as_completed(results):
            print(f.result())
    end=time.perf_counter()

    total_time=end-start

    print(f"Finished Executing in {round(total_time,2)} Second(s)")
```

**Output:**

```python
Process with ID: 10748 Sleeping 5 Second(s)...
Process with ID: 612 Sleeping 4 Second(s)...
Process with ID: 13900 Sleeping 3 Second(s)...
Process with ID: 10024 Sleeping 2 Second(s)...
Process with ID: 18612 Sleeping 1 Second(s)...
Process with ID: 18612 Done Sleeping 1 Second(s)..!
Process with ID: 10024 Done Sleeping 2 Second(s)..!
Process with ID: 13900 Done Sleeping 3 Second(s)..!
Process with ID: 612 Done Sleeping 4 Second(s)..!
Process with ID: 10748 Done Sleeping 5 Second(s)..!
Finished Executing in 5.13 Second(s)
```

## Without as_completed() method

- Prints the result of each process based on the order of execution started.

```python
import concurrent.futures
import time
import os

def do_something(sec):
    print(f"Process with ID: {os.getpid()} Sleeping {sec} Second(s)...")
    
    time.sleep(sec)
    return f"Process with ID: {os.getpid()} Done Sleeping {sec} Second(s)..!"

result=[]

if __name__=="__main__":

    start=time.perf_counter()
    processes=[]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds=[5,4,3,2,1]
        results=[executor.submit(do_something,sec) for sec in seconds]

        for process in results:
            print(process.result())  # print return result from target method.

    end=time.perf_counter()

    total_time=end-start

    print(f"Finished Executing in {round(total_time,2)} Second(s)")
```

**Output:**

```python
Process with ID: 22520 Sleeping 5 Second(s)...
Process with ID: 15632 Sleeping 4 Second(s)...
Process with ID: 15380 Sleeping 3 Second(s)...
Process with ID: 6644 Sleeping 2 Second(s)...
Process with ID: 2968 Sleeping 1 Second(s)...
Process with ID: 22520 Done Sleeping 5 Second(s)..!
Process with ID: 15632 Done Sleeping 4 Second(s)..!
Process with ID: 15380 Done Sleeping 3 Second(s)..!
Process with ID: 6644 Done Sleeping 2 Second(s)..!
Process with ID: 2968 Done Sleeping 1 Second(s)..!
Finished Executing in 5.15 Second(s)
```

## map()

```python
import concurrent.futures
import time
import os

def do_something(sec):
    print(f"Process with ID: {os.getpid()} Sleeping {sec} Second(s)...")
    
    time.sleep(sec)
    return f"Process with ID: {os.getpid()} Done Sleeping {sec} Second(s)..!"

result=[]

if __name__=="__main__":

    start=time.perf_counter()
    processes=[]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds=[5,4,3,2,1]
        results=executor.map(do_something,seconds)

        for result in results:
            print(result)  

    end=time.perf_counter()

    total_time=end-start

    print(f"Finished Executing in {round(total_time,2)} Second(s)")
```

**Output:**

```python
Process with ID: 22520 Sleeping 5 Second(s)...
Process with ID: 15632 Sleeping 4 Second(s)...
Process with ID: 15380 Sleeping 3 Second(s)...
Process with ID: 6644 Sleeping 2 Second(s)...
Process with ID: 2968 Sleeping 1 Second(s)...
Process with ID: 22520 Done Sleeping 5 Second(s)..!
Process with ID: 15632 Done Sleeping 4 Second(s)..!
Process with ID: 15380 Done Sleeping 3 Second(s)..!
Process with ID: 6644 Done Sleeping 2 Second(s)..!
Process with ID: 2968 Done Sleeping 1 Second(s)..!
Finished Executing in 5.15 Second(s)
```

### Example of using Multi-Processing

You are going to do some image processing on images and this involves some CPU Bound and IO Bound also.

**Using Multi processing:**

```python
import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

size = (1200, 1200)

def process_image(img_name):
    img = Image.open(f"download/{img_name}")

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'Processed/{img_name}')
    print(f'{img_name} was processed...')

if __name__=="__main__":
    t1 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)
    
    # normal way
    
    # for image in img_names:
    #     process_image(image)

    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')
```

**Output:**

```python
photo-1516117172878-fd2c41f4a759.jpg was processed...
photo-1516972810927-80185027ca84.jpg was processed...
photo-1524429656589-6633a470097c.jpg was processed...
photo-1522364723953-452d3431c267.jpg was processed...
photo-1530224264768-7ff8c1789d79.jpg was processed...
photo-1530122037265-a5f1f91d3b99.jpg was processed...
photo-1532009324734-20a7a5813719.jpg was processed...
photo-1541698444083-023c97d3f4b6.jpg was processed...
photo-1564135624576-c5c88640f235.jpg was processed...
photo-1550439062-609e1531270e.jpg was processed...
photo-1504198453319-5ce911bafcde.jpg was processed...
photo-1549692520-acc6669e2f0c.jpg was processed...
photo-1493976040374-85c8e12f0c0e.jpg was processed...
Finished in 4.099507700186223 seconds
```

**Normal way of using for loop:**

```python
import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

size = (1200, 1200)

def process_image(img_name):
    img = Image.open(f"download/{img_name}")

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'Processed/{img_name}')
    print(f'{img_name} was processed...')

if __name__=="__main__":
    t1 = time.perf_counter()
    
    # normal way
    for image in img_names:
        process_image(image)

    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')
```

**Output:**

```python
photo-1516117172878-fd2c41f4a759.jpg was processed...
photo-1532009324734-20a7a5813719.jpg was processed...
photo-1524429656589-6633a470097c.jpg was processed...
photo-1530224264768-7ff8c1789d79.jpg was processed...
photo-1564135624576-c5c88640f235.jpg was processed...
photo-1541698444083-023c97d3f4b6.jpg was processed...
photo-1522364723953-452d3431c267.jpg was processed...
photo-1493976040374-85c8e12f0c0e.jpg was processed...
photo-1504198453319-5ce911bafcde.jpg was processed...
photo-1530122037265-a5f1f91d3b99.jpg was processed...
photo-1516972810927-80185027ca84.jpg was processed...
photo-1550439062-609e1531270e.jpg was processed...
photo-1549692520-acc6669e2f0c.jpg was processed...
Finished in 12.215091899968684 seconds
```

## Conclusion

<aside>
💡 We Achieved 3X times faster Execution/Processing of code by using Multi-Processing.

</aside>

---

## Shared Memory in Multi Processing

---

**multiprocessing** module provides **Array** and **Value** objects to share data between processes.

- **Array:** a ctypes array allocated from **shared memory**.
- **Value:** a ctypes object allocated from **shared memory**.

```python
import multiprocessing

def square_list(mylist, result, square_sum):
	# append squares of mylist to result array
	for idx, num in enumerate(mylist):
		result[idx] = num * num

	# square_sum value
	square_sum.value = sum(result)

	# print result Array
	print("Result(in process p1): {}".format(result[:]))

	# print square_sum Value
	print("Sum of squares(in process p1): {}".format(square_sum.value))

if __name__ == "__main__":
	# input list
	mylist = [1,2,3,4]

	# creating Array of int data type with space for 4 integers
	result = multiprocessing.Array('i', 4)

	# creating Value of int data type
	square_sum = multiprocessing.Value('i')

	# creating new process
	p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

	# starting process
	p1.start()

	# wait until the process is finished
	p1.join()

	# print result array
	print("Result(in main program): {}".format(result[:]))

	# print square_sum Value
	print("Sum of squares(in main program): {}".format(square_sum.value))
```

**Output:**

```python
Result(in process p1): [1, 4, 9, 16]
Sum of squares(in process p1): 30
Result(in main program): [1, 4, 9, 16]
Sum of squares(in main program): 30
```

---

## Manger for Server Process

---

**multiprocessing** module provides a **Manager** class which controls a server process.

Manger can be made to support arbitrary object types like lists, dictionaries, Queue, Value, Array, etc. Also, a single manager can be shared by processes on different computers over a network. They are, however, slower than using shared memory.

### Manager

```python
import multiprocessing

def print_records(records):
	for record in records:
		print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))

def insert_record(record, records):
	records.append(record)
	print("New record added!\n")

if __name__ == '__main__':
	with multiprocessing.Manager() as manager:
		# creating a list in server process memory
		records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)])

		# new record to be inserted in records
		new_record = ('Jeff', 8)

		# creating new processes
		p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
		p2 = multiprocessing.Process(target=print_records, args=(records,))

		# running process p1 to insert new record
		p1.start()
		p1.join()

		# running process p2 to print records
		p2.start()
		p2.join()
```

**Output:**

```python
New record added!

Name: Sam
Score: 10

Name: Adam
Score: 9

Name: Kevin
Score: 9

Name: Jeff
Score: 8
```

---

## Locks in Multi Processing

---

Concurrent accesses to shared resource can lead to **race condition**.

**Race condition** Occurs when two or more processes access the shared resource and try to change it Concurrently. As a result the shared resource value may be unpredictable or vary depending on the context switches between processes.

To avoid this race condition you have to use **LOCK**s. **Lock** is implemented using a **Semaphore** 

object provided by the Operating System.

A **semaphore** is a synchronization object that controls access by multiple processes to a common resource in a parallel programming environment.

**Example:** 

This code is to do transactions like withdraw and deposit 1000 times each for 10 times with inital shared variable set to 100.

Since, we created a process p1 and p2 for each **withdraw** and **deposit** methods respectively.

This processes concurrently accesses the **balance** shared variable.

### Without Locks

```python
import multiprocessing

def withdraw(balance):
    for _ in range(1000):
        balance.value-=1

def deposit(balance):
    for _ in range(1000):
        balance.value+=1

def perform_transactions():
    balance=multiprocessing.Value("i",100)

    p1=multiprocessing.Process(target=withdraw,args=(balance,))
    p2=multiprocessing.Process(target=deposit,args=(balance,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final Balance: ",balance.value)

if __name__=="__main__":

    for _ in range(10):
        perform_transactions()
```

**Output:**

```python
Final Balance:  497
Final Balance:  100
Final Balance:  100
Final Balance:  56
Final Balance:  277
Final Balance:  -623
Final Balance:  -345
Final Balance:  41
Final Balance:  -382
Final Balance:  -84
```

### With Locks

```python
import multiprocessing

def withdraw(balance,lock):
    for _ in range(1000):
        lock.acquire()
        balance.value-=1
        lock.release()

def deposit(balance,lock):
    for _ in range(1000):
        lock.acquire()
        balance.value+=1
        lock.release()

def perform_transactions():
    balance=multiprocessing.Value("i",100)
    
    lock=multiprocessing.Lock()

    p1=multiprocessing.Process(target=withdraw,args=(balance,lock,))
    p2=multiprocessing.Process(target=deposit,args=(balance,lock,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final Balance: ",balance.value)

if __name__=="__main__":

    for _ in range(10):
        perform_transactions()
```

**Output:**

```python
Final Balance:  100
Final Balance:  100
Final Balance:  100
Final Balance:  100
Final Balance:  100
Final Balance:  100
Final Balance:  100
Final Balance:  100
Final Balance:  100
Final Balance:  100
```

---

## Pooling

---

Pooling involves sharing a task among all cores instead of running a task on single core.

This allows to make use of CPU Cores effectively.

Decreases the CPU cores idle time.

The multiprocessing module in Python provides the Pool class which can be used to create a pool of processes. This class automatically creates processes for the user and distributes tasks among the cores of the CPU. This means that as a user you can execute your code in parallel without explicitly having to create the processes yourself. Moreover, the Pool class also provides a simple interface for asynchronous execution of functions, allowing you to easily execute a large number of tasks in a concurrent and efficient manner. Overall, the Pool class is a powerful tool for any Python developer looking to speed up their code and make use of the multi-core capabilities of modern CPUs.

```python
import multiprocessing

def square(num):
    return num*num

if __name__=="__main__":

    lst=[1,2,3,4,5,6]

    p=multiprocessing.Pool()
    result=p.map(square,lst)

    print(result)
```

Output:

```python
[1, 4, 9, 16, 25, 36]
```

---

## Resources

- An [**Article**](https://www.geeksforgeeks.org/processpoolexecutor-class-in-python/) about Process Pool from GFG.
- An **[Article](https://www.geeksforgeeks.org/multiprocessing-python-set-1/)** about Multi Processing from GFG.
- A YouTube **[Video](https://youtu.be/fKl2JW_qrso?si=EgzqHwsv6z6f2YKy)** From Corey Schafer Channel.