# Databricks notebook source
The term "polymorphism" means "many forms," and in Python, it allows the same operation or method to behave differently depending on the object it is acting upon.

# COMMAND ----------

Polymorphism

1.overloading
. Operator overloading
. method overloading
. constructor overloading

2.overriding
. method overiding
. constructor overiding


# COMMAND ----------

#Method Overloading

# If 2 methods having same name but different type of arguments then are said t those method so
# be overloaded methods.But in Python Method overloading is not possible.
# If we are trying to declare multiple methods with same name and different number of arguments
# then Python will always consider only last method.


# COMMAND ----------

class cal:

    def add(self,a,b):
        print(a+b)
    
    def add(self,a,b,c):
        print(a+b+c)

    def add(self,a,b,c,d):
        print(a+b+c+d)

op = cal()
# op.add(1,2)  ---> error: missing 2 required positional arguments: 'c' and 'd'
op.add(1,2,3,4)

# COMMAND ----------

class cal:

    def add(self,*num):
        total = 0
        for i in num:
            total = total+i
            
        print(total)

op = cal()
op.add(1,2)

# COMMAND ----------

# constructor overloading

# Constructor overloading is not possible in Python.
# If we define multiple constructors then the last constructor will be considered.
# Note: Based on our requirement we can declare constructor with default arguments and variable
# number of arguments.


# COMMAND ----------

class emp:

    def __init__(self):
        print("Hi")

    def __init__(self,a):
        self.a = a
        print(f"Hi and value is {a}")

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(f"Hi and values are {self.a},{self.b}")

#ob = emp() -- Error :  __init__() missing 2 required positional arguments: 'a' and 'b'
#ob = emp(1) -- Error : __init__() missing 1 required positional argument: 'b'
ob = emp(1,2)

# COMMAND ----------

# Method Overiding

# The method in the child class must have the same name, parameters, and return type as the method in the parent class
# Overriding is commonly used to provide specific implementations while keeping the same interface.
# use the super() function to call the parent class's method from the child class.


# COMMAND ----------

class Parent:
    def display_message(self):
        print("This is a message from the Parent class.")

class Child(Parent):
    def display_message(self):
        print("This is a message from the Child class.")

# Example usage
#parent_obj = Parent()
child_obj = Child()

#parent_obj.display_message()  # Output: This is a message from the Parent class.
child_obj.display_message()   # Output: This is a message from the Child class.


# COMMAND ----------

class Parent:
    def display_message(self):
        print("This is a message from the Parent class.")

class Child(Parent):
    def display_message(self):
        super().display_message()  # Call the parent class method
        print("This is a message from the Child class.")

# Example usage
child_obj = Child()
child_obj.display_message()

# COMMAND ----------

Key Points About Constructor Overriding

__init__ Method: The constructor in Python, automatically called when an object is created.

Overriding: The child class provides its own implementation of the __init__ method.

Using super(): Allows calling the parent class’s __init__ method within the child class.

# COMMAND ----------

class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent class constructor called. Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        # Override the parent class constructor
        super().__init__(name)  # Call the parent class constructor
        self.age = age
        print(f"Child class constructor called. Age: {self.age}")

# Example usage
child_obj = Child("Alice", 10)
