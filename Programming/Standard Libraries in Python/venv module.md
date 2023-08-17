# venv module

### What is a Virtual Environment

> A cooperatively isolated runtime environment that allows Python users and applications to install and upgrade Python distribution packages without interfering with the behavior of other Python applications running on the same system.
> 

### Use of Virtual Environment

- Allows us to use project specific dependencies/packages without causing any inconvenience to global packages.
- No Security Risks: Installing Packages Globally Causes Security risks, in case of package contains any malware.
- No more Conflicts between project specific package dependencies and Global packages.
- On updating global packages, make sure that local dependencies does not break Compatibility i.e.; overcomes code incompatibility.

## Mange Virtual Environment in Python using venv Module

---

- venv is a module provided by Python in Standard library from Python3.3 to create and manage Virtual Environments. Version below Python3.3 make use virtualenv library.
- Different Python Projects will sometimes need a specific version of a library. So, It is not possible that one python installation to meets the requirement of every application.
- This arises a problem called **“**requirement conflict**”**.
- The solution to this problem is Virtual Environments

### How To Create Virtual Environment

> python -m venv "**virtual_environment_name”**
> 

### Create Virtual Environment with particular version of python

lets say 3.6,

> python3.6 -m venv "**virtual_environment_name”**
> 

### How to activate Virtual Environment

> **virtual_environment_name**\Scripts\activate.bat
> 

for mac / Unix

> source **virtual_environment_name**/bin/activate
> 

### How to deactivate Virtual Environment

> deactivate
> 

### How to delete an entire Virtual Environment

> rmdir **virtual_environment_name** /s
> 

for macOS / Unix

> rmdir -r **virtual_environment_name**
> 

### How to create a Virtual Environment

> python -m venv **virtual_environment_name** --system-site-packages
> 

### To list out local packages of Virtual Environment

> pip list --local
> 

## Manage Packages with pip

---

### To list out available packages

> pip list
> 

### To show detailed info about particular package

> pip show **package_name**
> 

### To Install particular package with latest version

> pip install **package_name**
> 

### To install particular package with specific version

> pip install **package_name**==**version**
> 

### To upgrade particular package to latest version or specific version

> pip install  - -upgrade **package_name[==version]**
> 

### To list out the installed packages with version

> pip freeze
> 

> pip freeze >requirements.txt
> 

### What is requirements.txt file

> The requirements.txt contains all the project dependencies and this is committed to version control and shipped as part of an application to the user.
> 

It is a common convention is to store the necessary package names with version required for any application / environment. So that users can be installed them easily.

### To install a packages from a requirements.txt file

> pip install -r requirements.txt
> 

## Resources:

- Check out the [**video**](https://youtu.be/APOPm01BVrk) from Corey Schafer You tube Channel.
- Check out the official [**documentation](https://docs.python.org/3/tutorial/venv.html)**