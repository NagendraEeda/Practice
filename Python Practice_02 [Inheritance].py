# Databricks notebook source
# MAGIC %md
# MAGIC > **Inheritance**
# MAGIC -  single Inheritance
# MAGIC - Multiple Inheritance
# MAGIC - Multilevel Inheritance
# MAGIC - Hierarchical Inheritance

# COMMAND ----------

# Single Inheritance: A child class inherits from a single parent class.

class parent:

    def show_parent(self):
        print("iam parent")

class child(parent):

    def show_child(self):
        print("iam child")

user1 = child()

user1.show_child()
user1.show_parent()

# COMMAND ----------

# Multiple Inheritance: A child class inherits from multiple parent classes.
class parent1:

    def show_parent1(self):
        print("Iam Parent 1")
class parent2:

    def show_parent2(self):
        print("Iam parent2")

class child(parent1,parent2):
    
    def show_child(self):
        print("iam child")

user2 = child()

user2.show_child()
user2.show_parent1()
user2.show_parent2()

# COMMAND ----------

# **Multilevel Inheritance: A child class inherits from a parent class, which itself inherits from another parent class.**

class grandfather:
    
    def show_grandfather(self):
        print("Iam Grand Father I have House")

class father(grandfather):
    
    def show_father(self):
        print("I am father and i Have a Car")

class child(father):
    
    def show_child(self):
        print("Iam child and i have a bike")

user3 = child()

user3.show_child()
user3.show_father()
user3.show_grandfather()

# COMMAND ----------

# **Hierarchical Inheritance: Multiple child classes inherit from the same parent class.**

class parent:

  def show_parent(self):
    print("Iam Parent i have house")

class child1(parent):

  def show_child1(self):
    print("Iam first child and i have car")

class child2(parent):

  def show_child2(self):
    print("Iam Second child and I have a bike")


user4 = child1()
user4.show_child1()
user4.show_parent()
#user4.show_child2() ---> it doesn't work 


user5 = child2()
user5.show_child2()
user5.show_parent()
#user5.show_child1() --> it doesn't work


# COMMAND ----------

# ** Hybrid Inheritance: A combination of two or more types of inheritance.**

class Parent:
    def show_parent(self):
        print("This is the Parent class")

class Child1(Parent):
    def show_child1(self):
        print("This is Child1 class")

class Child2:
    def show_child2(self):
        print("This is Child2 class")

class Child3(Child1, Child2):  # Hybrid inheritance
    def show_child3(self):
        print("This is Child3 class")

# Example usage
child3_obj = Child3()
child3_obj.show_parent()
child3_obj.show_child1()
child3_obj.show_child2()
child3_obj.show_child3()