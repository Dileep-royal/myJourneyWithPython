# Modules in Python

**Module:**

In simple, module is nothing but an individual python file used in a project.

**Use Case:**

You have several modules in a project, Suppose we need to use a specific method or variable of other module in any particular module. Then we can simple access those required things by importing a module.

**Advantages:**

- Code reusability
- Decrease in No. of lines of code

<aside>
💡 **Note:**                                                                                                                                          If we have any print statements in source module those are executed automatically. This is because it includes all the code in to destination module.

</aside>

## **Accessing Python Modules**

File Structure example:

### From **Same Directory**

- Accessing a modules from same directory is straightforward and simple to do.
- Suppose, you have two modules named with **module1.py** and **module2.py** with in the same folder called hg **folder1**.
- In **module1.py** contains a method **evenNumbersUptoN()** and Variable namely **sampleVariable** .
- In **module2.py** you want to use methods and variables of **module1.py** then, you can simply import required things from **module1.py** using “import” keyword.

**Snapshot of module1.py:**

![Screenshot 2023-08-15 102222.png](Modules%20in%20Python%206462a68011034d2fb9504aae183033ba/Screenshot_2023-08-15_102222.png)

**Snapshot of module2.py:**

![Screenshot 2023-08-15 102707.png](Modules%20in%20Python%206462a68011034d2fb9504aae183033ba/Screenshot_2023-08-15_102707.png)

### From Different Directory

- For Example, you have two modules named with **module3.py** in the folder called **folder2** and **module2.py** with in the folder called **folder1**.
- In **module3.py** contains a method **oddNumbersUptoN()**.
- In **module2.py* you want to use methods and variables of **module3.py** then, you can simply import required things from **lmodule3.py** using “import” keyword.

**Snapshot of module2.py:**

![Screenshot 2023-08-15 102707.png](Modules%20in%20Python%206462a68011034d2fb9504aae183033ba/Screenshot_2023-08-15_102707.png)

**Snapshot of module3.py:**

![Screenshot 2023-08-15 102200.png](Modules%20in%20Python%206462a68011034d2fb9504aae183033ba/Screenshot_2023-08-15_102200.png)

- Suppose you have source module in different directory, then to access that they are two ways.
- They are:
    - Using sys module
    - Set a path to Python Environment variable “PYTHONPATH”
1. **Using sys module**
- sys module have path list that contains the paths to different modules.
- Simply add path of source module i.e.; **folder2** to **sys.path** list using append() list method.
- But it is not a best practice.
- **Code to set sys.path:**

```python
import sys
#Code to access modules from outside of folder and from another folder
sys.path.append("C:/Users/MSI/Desktop/Python/folder2")
```

1. **Set a module path to Python Environment variable “PYTHONPATH”**
- Add a path of python source module to PYTHONPATH environment variable.
- Steps to add new environment variable.
    1. In window search bar, search for Advanced System Settings.
    2. Upon Opening Advanced System Settings tab, then click on Environment Variables button.
    3. In Environment Variables tab, Click on new user variable button.
    4. In new user Variable tab, Enter Variable Name as “**PYTHONPATH**” and set Variable Value to path of source module i.e.; **folder2**.
- *** of "PYTHONPATH" Environment Variable:

![Screenshot 2023-08-15 103106.png](Modules%20in%20Python%206462a68011034d2fb9504aae183033ba/Screenshot_2023-08-15_103106.png)