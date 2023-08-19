# File Handling

File handling involves creating files, reading from files and writing into files.

## Create a File object

- To create file object, we can make use of **open()** method and it requires two arguments file name(or) file path and a flag that specifies mode.
- **Different flag modes:**
    - x   → used to create a file if not existed already.
    - r    → opens the file in read only mode.
    - r+  → opens the file to read & write.
    - w   → opens the file in write only mode.
    - w+ → opens the file to read & write.
    - a    → opens the file in write mode to write into existing data.
    - a+ → opens  the  file to read and to write into existing data.
- All the above modes are human readable formats.
- For every mode specified above we also have binary format.
- They are rb, rb+, wb, wb+, ab, ab+.

we are using a file called **sample.txt** to demonstrate examples.

```
1) My Name is Dileep
2) My Age is 21
3) I recently Graduted in B.Tech in Computer Science and Engineering.
4) My skills are C, Python, Java, SQL, HTML, CSS,Git & Linux.
5) I'm Looking for a Job
```

**Syntax:**

```
file_obj=open(file_name,flag)
```

### → open()

- using flag mode “x” to create a new file.

```python
new_file=open("new_file.txt","x")
```

- Opening already existed file.
- If the file we are looking for is not available then it causes an **FileNotFoundError**.

```python
file_object=open("sample.txt","r+") # file object is created with r+ flag mode
```

## Opening files with Context Manager

- We have to close file at the end explicitly using close() method. If we didn’t, this causes leaks and max allowed file descriptors in system are reached and throws an error.
- Best way to open file is using **Context Manager** this implicitly close the file and allows to work freely of not to worry about file closing.

Here is an example to open files with context Manager.

```python
with open("sample.txt","a") as f:
    f.write("6) I am passionate about Python")
```

### Output

```
1) My Name is Dileep
2) My Age is 21
3) I recently Graduted in B.Tech in Computer Science and Engineering.
4) My skills are C, Python, Java, SQL, HTML, CSS,Git & Linux.
5) I'm Looking for a Job
6) I am passionate about Python
```

## Reading a data from a file using file object

To read a data  from a file object we can make use of read(), readline(), readlines() methods.

We have some other methods to have a more control over the file.

They are seek(),tell()

### → read()

- read() method reads the entire data of a file.
- this can also accept size i.e.; 100 reads first 100 characters

```python
file1.read(100)  # reads first 100 characters
```

### Output

```
1) My Name is Dileep. 
2) My Age is 21.
3) I recently Graduted in B.Tech in Computer Science and En
```

### → tell()

- Tells us the position of the file.

```python
with open("sample.txt","r") as f:
    first10Ch=f.read(10)
    print(first10Ch)
    print("The position now After reading 10 Characters:",f.tell())
    From10to20Ch=f.read(10)
    print(From10to20Ch)
    print("The position now After reading 10 Characters from previous position:",f.tell())
```

### Output

```python
1) My Name
The position now After reading 10 Characters: 10
 is Dileep
The position now After reading 10 Characters from previous position: 20
```

### → seek()

- By default, it size set to 0.
- Used to reposition the file position.
- It may used to set to starting of the file or some particular position.

```python
with open("sample.txt","r") as f:
    first10Ch=f.read(10)
    print(first10Ch)
    print("The position now After reading 10 Characters:",f.tell())
    f.seek(0)  # repositioned back to starting of the file
    repos=f.read(10)
    print("After repositioning back to starting of file:")
    print(repos)

    # If we want to jump to the particular position and to read
    print("Changing position to certain")
    f.seek(34) # repositions to 34 character
    from34to44ch=f.read(10)
    print("reading from 34 to 44 characters:")
    print(from34to44ch)
```

### Output

```
1) My Name
The position now After reading 10 Characters: 10
After repositioning back to starting of file:
1) My Name
Changing position to certain
reading from 34 to 44 characters:
is 21.
3)
```

### → readline()

- readline() method read the data line by line.
- After each readline() method execution the position is set to next line starting.

```python
with open("sample.txt","r") as f:
    firstLine=f.readline()
    print("First Line:\n",firstLine)
    secondLine=f.readline()
    print("Second Line:\n",secondLine)
```

### Output

```python
First Line:
 1) My Name is Dileep.

Second Line:
 2) My Age is 21.
```

### → readlines()

- It gives us the list of all lines.

```python
with open("sample.txt","r") as f:
    allLines=f.readlines()
    print(allLines)
```

### Output

```python
['1) My Name is Dileep. \n', '2) My Age is 21. \n', '3) I recently Graduted in B.Tech in Computer Science and Engineering.\n', '4) My skills are C, Python, Java, SQL, HTML, CSS,Git & Linux.\n', '5) I am Looking for a Job.\n']
```

## Writing the data into a file

By using write() method we can write into a file. For this to happen the file object should be opened in write mode.

### → write()

- Used to write into the file.

Below code is to write multiple lines in to a file.

```python
file1=open("sample.txt","w")
str1="1) My Name is Dileep. /n 2) My Age is 21. /n 3) I recently Graduted in B.Tech in Computer Science and Engineering. /n 4) My skills are C, Python, Java, SQL, HTML, CSS,Git & Linux. /n 5) I am Looking for a Job."
lst=str1.split(" /n ")
for line in lst:
    file1.write(line+"\n")
```

### Output

```
1) My Name is Dileep
2) My Age is 21
3) I recently Graduted in B.Tech in Computer Science and Engineering.
4) My skills are C, Python, Java, SQL, HTML, CSS,Git & Linux.
5) I'm Looking for a Job
```

### → writelines()

- This method allow us to pass a Iterables like list of strings, etc.
- It is better to use writelines() method instead of using write() while writing multiple lines.

Below code is to write multiple lines in to a file using writelines() method instead of using write().

```python
file1=open("sample.txt","w")
lst=['1) My Name is Dileep. \n', '2) My Age is 21.\n', '3) I recently Graduted in B.Tech in Computer Science and Engineering.\n', '4) My skills are C, Python, Java, SQL, HTML, CSS,Git & Linux.\n', '5) I am Looking for a Job.\n']
file1.writelines(lst)
```

### using seek() in writing:

- It only overwrites specified position.

### Working with images

- incase of reading and writings images date open them in binary format.

# use case:

- Copying & moving one file to another.
- Adding more pixels to images.

# Resources:

- [**Article**](https://www.freecodecamp.org/news/file-handling-in-python/) from freecodecamp .
- You Tube [**Video**](https://youtu.be/Uh2ebFW8OYM) from Corey Schafer Channel