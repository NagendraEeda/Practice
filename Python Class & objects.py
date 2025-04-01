# Databricks notebook source
# MAGIC %md
# MAGIC ![Object%20oriented%20programming.jpg](attachment:Object%20oriented%20programming.jpg)

# COMMAND ----------

# MAGIC %md
# MAGIC # What is Class and object ?
# MAGIC * __class__: In Object Oriented Programming, a Class is a blueprint for an object. 
# MAGIC * __object__: object is an instance of a class which has the structure of its blueprint but also owns its unique state and behaviour.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Types of variables
# MAGIC
# MAGIC * __class variable__: A variable that is shared by all instances of the class. class variables are not used as frequently as   instance variables are.
# MAGIC
# MAGIC * __Instance variable__ or attributes – data that belongs to individual objects; every object has its own copy of each one.
# MAGIC
# MAGIC ## Types of methods 
# MAGIC
# MAGIC * An object has __attributes__ and __behaviours__. These behaviours are called methods in programming
# MAGIC * __instance method__ These are so called because they can access unique data of their instance.
# MAGIC * __class method__ Class methods don’t need self as an argument, but they do need a parameter called cls. This stands for class, and like self, gets automatically passed in by Python
# MAGIC * __static methods__ This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters)

# COMMAND ----------

# MAGIC %md
# MAGIC ![Copy%20of%20Simple%20Business%20Organizational%20Chart.png](attachment:Copy%20of%20Simple%20Business%20Organizational%20Chart.png)

# COMMAND ----------

# MAGIC %md
# MAGIC # Creating class objects

# COMMAND ----------

# MAGIC %md
# MAGIC **__init__(self) function**
# MAGIC
# MAGIC * All classes have a function called __init__ ()function to assign values to obeject properties, or other operations.
# MAGIC
# MAGIC **Self parameter**
# MAGIC * The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# COMMAND ----------

class moblie:
    
    def __init__(self):
        print("I am init method")
    
    def purchase(self, name,ram):
        print(f'Thanks for purchasing {name} with {ram}')

# COMMAND ----------

# 1 - create an object 
# 2 - initialize the values to the instance variable
# constructor will help to create variables in one line 
# __init_() method is also called as constructor method
# while  creating a object it will check __init__() method is written if written then it will be called automatically 


john = moblie()# this step will automatically call the constructor if  __init__() method is present in class
john.brand = 'samsung'
john.ram = "8Gb"
john.purchase(john.brand, john.ram)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Instance variable

# COMMAND ----------

# MAGIC %md
# MAGIC * __Instance variable__  – instance variable is nothing but the variable belongs to object or instance called as instance variable or simply instance variable is a variable that is bound to object itself.
# MAGIC

# COMMAND ----------

class mobile:
    
    def __init__(self, name, ram):
        #instance variable
        self.name = name
        self.ram = ram
        
# Creating object
m1 = mobile("oppo", "4")
print(m1.name, m1.ram)

m2 = mobile("realme", "8")
print(m2.name, m2.ram)

# COMMAND ----------

# MAGIC %md
# MAGIC ## class variable:

# COMMAND ----------

# MAGIC %md
# MAGIC * __class variable__: A variable that is shared by all instances of the class. class variables are not used as frequently as   instance variables are.

# COMMAND ----------

class mobile:
    
    #class variable
    Charger = "yes"
    
    def __init__(self, name, ram):
        #instance variable
        self.name = name
        self.ram = ram

print("object 1")
m1 = mobile("oppo", "4")
print(m1.name, m1.ram)
print(m1.Charger)

print("-----------------------------------")

print("object 2")
m2 = mobile("realme", "8")
print(m2.name, m2.ram)
print(mobile.Charger)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Instance method

# COMMAND ----------

# MAGIC %md
# MAGIC * __instance method__ Instance method belong to the Object of the class not to the class. so, they can be called after creating the Object of the class.

# COMMAND ----------

class mobile:
    
    #class variable
    wireless_charging = "yes"
    
    def __init__(self, name, ram):
        #instance variable
        self.name = name
        self.ram = ram
        
    #instance method     
    def display(self):
        print(f"Name :{ self.name}\nram :{self.ram}")
              

print("object 1")
m1 = mobile("oppo", "4")
print(m1.name, m1.ram)
m1.display()

print("-----------------------------------")

print("object 2")
m2 = mobile("realme", "8")
print(m2.name, m2.ram)
m2.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Class method

# COMMAND ----------

# MAGIC %md
# MAGIC * __class method__ Class methods don’t need self as an argument, but they do need a parameter called cls. This stands for class, and like self, gets automatically passed in by Python

# COMMAND ----------

class mobile:
    
    #class variable
    wireless_charging = "yes"
    
    def __init__(self, name, ram):
        #instance variable
        self.name = name
        self.ram = ram
        
    #instance method     
    def display(self):
        print(f"Name :{ self.name}\nram :{self.ram}")
    
    @classmethod    
    def verification(cls):
        return f'Charger :{cls.wireless_charging}'
    
    
print("object 1")
m1 = mobile("oppo", "4")
print(m1.verification())
m1.display()

print("-----------------------------------")

print("object 2")
m2 = mobile("realme", "8")
print(m2.verification())
m2.display()


# COMMAND ----------

# MAGIC %md
# MAGIC ## static method

# COMMAND ----------

# MAGIC %md
# MAGIC * __static methods__ This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters)
# MAGIC * Note: It will be helpfull when we want to access other class objects

# COMMAND ----------

class mobile:
    
    #class variable
    wireless_charging = "yes"
    
    def __init__(self, name, ram):
        #instance variable
        self.name = name
        self.ram = ram
        
    #instance method     
    def display(self):
        print(f"Name :{ self.name}\nram :{self.ram}")
        
    @classmethod    
    def verification(cls):
        return f'Charger :{cls.wireless_charging}'
    
    @staticmethod
    def get_name(): 
        print("Name is correct")
            
m1 = mobile("oppo", "8")
print(mobile.wireless_charging)
print(m1.verification())
m1.get_name()
m1.display()

print("_______________________________")

m2 = mobile("realme", "4")
print(mobile.wireless_charging)
print(m2.verification())
m2.get_name()
m2.display()



# COMMAND ----------

# MAGIC %md
# MAGIC # Complete Variables and methods

# COMMAND ----------

class mobile:
    
    #class variable
    wireless_charging = "yes"
    
    def __init__(self, name, ram):
        #instance variable
        self.name = name
        self.ram = ram
        
    #instance method     
    def display(self):
        print(f"Name :{ self.name}\nram :{self.ram}")
        
    @classmethod    
    def verification(cls):
        return cls.wireless_charging
    
    @staticmethod
    def get_name(): 
        print("I am static method")
        
        
m1 = mobile("oppo", "8")
print(mobile.wireless_charging)
print(m1.verification())
m1.get_name()
m1.display()

print("_______________________________")

m2 = mobile("realme", "4")
print(mobile.wireless_charging)
print(m2.verification())
m2.get_name()
m2.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # More Examples

# COMMAND ----------

class Student:
    
    def __init__(self,name,age, **marks):
        self.name = name 
        self.age = age 
        self.marks = marks
        
    def display(self):
        print("Name-", self.name)
        print("age- ", self.age)
        print("Marks- ", self.marks)

# COMMAND ----------

s1 = Student("john", 25, first=560, second=260)
s1.display()

# COMMAND ----------

class employees:
    
    empcount = 0 
    
    def __init__(self, Name, Salary):
        self.Name = Name
        self.Salary = Salary
        employees.empcount += 1
        
    def displayCount(self):
        print("Total Employee %d" % employees.empcount)
        
    def Displayemployee(self):
        print ("Name ", self.Name, "Salary",self.Salary)
        
emp1 = employees("Rakesh",4000)
emp2 = employees("Anuhya", 3000)
emp1.Displayemployee()
emp2.Displayemployee()
print("Total count", employees.empcount)