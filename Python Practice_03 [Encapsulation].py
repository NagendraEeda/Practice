# Databricks notebook source
# MAGIC %md
# MAGIC > Encapsulation :  is a process of wrapping the both methods and variables

# COMMAND ----------

# MAGIC %md
# MAGIC - Public: Attributes and methods accessible anywhere.
# MAGIC
# MAGIC - Protected: Attributes and methods prefixed with _, intended for use within the class and its subclasses.
# MAGIC
# MAGIC - Private: Attributes and methods prefixed with __, restricting access outside the class.

# COMMAND ----------

class employee:

    def __init__(self,name,age,salary):
        self.name = name # Public
        self._age = age # Protected
        self.__salary = salary # Private

ob = employee("Sam",20,2000)
print(ob.name)
print(ob._age)
#print(ob.salary) ---> Throw an error
print(ob._employee__salary)  ---> one way to access private variables but not recommended


# COMMAND ----------

# MAGIC %md
# MAGIC -  Setters and Getters in Python are methods used to control access to private attributes of a class. 
# MAGIC - They allow the programmer to read (get) or modify (set) the value of private attributes while maintaining control over the logic of how those attributes are accessed or changed

# COMMAND ----------

class employee:

    def __init__(self,name,age,salary):
        self.name = name # Public
        self._age = age # Protected
        self.__salary = salary # Private
    
    #getter
    def get_salary(self):
        return self.__salary 
    
    #setter
    def set_salary(self,newsalary):
        self.__salary = newsalary

ob = employee("Sam",20,2000)
ob.get_salary()

#setter
print(ob.set_salary(1000))
ob.get_salary()



# COMMAND ----------

class employee:

    def __init__(self):
        print("Im constructor")

    def _verification(self):
        print("Iam a Prected Method")

class subemployee(employee):
    def verification(self):
        self._verification()

ob = employee() # only construcotr will execute

ob._verification() #getting ana error 

subemp = subemployee()
subemp.verification()

# COMMAND ----------

class Parent:
    def __init__(self, name):
        self.name = name

    def _protected_method(self):
        print(f"This is a protected method in {self.name}'s class.")

class Child(Parent):
    def call_protected(self):
        # Calling the protected method from the parent class
        self._protected_method()

# Example usage
parent_obj = Parent("Parent")
parent_obj._protected_method()  # Accessing the protected method directly

child_obj = Child("Child")
child_obj.call_protected()      # Calling the protected method via child class