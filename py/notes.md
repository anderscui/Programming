

**getting help**

help(int) / help(1)
pydoc int


**modules**

The import statement creates a new namespace and executes all the statements in the associated .py file within
    that namespace. To access the contents of the namespace after import, simply use module.member_name.
    
dir() lists the contents of a module.

**objects**

object is the root of all Python types. Methods are defined using the def statement. 
The first argument in each method always refers to the object itself.
By convention, self is the name used for this arg.
  
All operations involving the attributes of an object must explicitly refer to the self var.

Methods with leading and trailing double underscores are special methods, e.g. __init__

- @staticmethod decorator


**strings**

strings are stored as seq of chars indexed by integers.

**reg ex**

* match (from start of string)
* search
* findall
* finditer

**errors and exceptions**

Normally, errors cause a program to terminate. However, you can catch and handle exceptions using try and except.

The with statement is normally only compatible with objects related to system resources or the execution environment
    such as files, connections, and locks. However, user-defined objects can define their own custom processing.
    

**data structures**

**list** in Python is similar to the generic **List<T>** type in C#, it's mutable.

**tuple**s are immutable, they are usually used in cases where a statement or a func can safely assume that 
    the collection of values i.e. the tuple of values will not change. In C#, there is also a generic type **tuple<T>**.

**lists**, **tuples** and **strings** are examples of sequences, what are common to them?

**dicts** are probably the most finely tuned data type in the Python interpreter. So you are almost always better off
 using a dictionary than trying to come up with some kind of custom data structure on your own. 




