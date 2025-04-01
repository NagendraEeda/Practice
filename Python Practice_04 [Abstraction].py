# Databricks notebook source
#We use Abstraction for hiding the internal details or implementations of a function and showing its functionalities only.
"""
Any class with at least one abstract function is an abstract class. 
In order to create an abstraction class first, you need to import ABC class from abc module. 
This lets you create abstract methods inside it. ABC stands for Abstract Base Class.
from abc import ABC, abstractmethod
"""

#parent is the abstract class that inherits from the ABC class from the abc module.

# COMMAND ----------

# Normal 
class animal:

    def __init__(self):
        pass

    def make_sound(self):
        pass

class dog(animal):
    pass
    
class cat(animal):
    pass
    
firstanimal = dog()
#firstanimal.make_sound()

>> Here we can call the child class without calling any methods
>> but in abstraction we can't do that


# COMMAND ----------

from abc import ABC,abstractmethod
class animal(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class dog(animal):
    pass

class cat(animal):

    def make_sound(self):
        return "meow"
    
#firstanimal = dog() --> it doesn't work beacause make sound method is abstract we need to use that in child class
firstanimal = cat()
firstanimal.make_sound()