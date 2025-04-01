# Databricks notebook source
# MAGIC %md
# MAGIC # Association
# MAGIC - Composition and aggregation are specialised form of Association. 
# MAGIC - Whereas Association is a relationship between two classes without any rules.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Composition(HAS - A Relation) Strong Association
# MAGIC
# MAGIC - In composition, one of the classes is composed of one or more instance of other classes.
# MAGIC - In other words, one class is container and other class is content and if you delete the container object then all of its      contents objects are also deleted.

# COMMAND ----------

# MAGIC %md
# MAGIC ### example 1

# COMMAND ----------

class myntra:
    def __init__(self):
        print("Welcome to myntra")
        self.m = self.Mens()
        self.w = self.womens()

    class Mens:
        def __init__(self):
            print("welcome to mens section")

        class footware:
            def __init__(self):
                print("welcome to mens footware")

            def woodland(self):
                print("Thanks for searching woodland")

            def crocs(self):
                print("thanks for searching crocs")

        class clothing:
            def __init__(self):
                print("welcome to clothing")

            def Gstar(self):
                print("thanks fot searching Gstar")


    class womens:
        def __init__(self):
            print("welcome to women section")

        class footware:
            def __init__(self):
                print("welcome to  women footware")

            def woodland(self):
                print("Thanks for searching woodland")

            def crocs(self):
                print("thanks for searching crocs")

        class clothing:
            def __init__(self):
                print("welcome to clothing")

            def Gstar(self):
                print("thanks fot searching Gstar")

shopping = myntra()
shopping.m.footware().crocs()
shopping.w.clothing().Gstar()
                        
# shoping = myntra()
# men = shoping.Mens()
# foot = men.footware()
# foot.woodland()


# women = shoping.womens()
# foot1 = women.footware()
# foot1.woodland()

# COMMAND ----------

# MAGIC %md
# MAGIC ### example 2

# COMMAND ----------

class processor:
    def processor_info(self):
        print("Thanks for using processor")

class camera:
    def camera_info(self):
        print("Thanks for using dual cameras")

class mobile_display:
    def mobile_display_info(self):
        print("thanks for using our dispaly")


class iphone:
    def __init__(self):
        self.processor = processor()
        self.camera = camera()
        self.mobile_display = mobile_display()

    def total_info(self):
        print("Welcome to iphone ")
        self.processor.processor_info()
        self.camera.camera_info()
        self.mobile_display.mobile_display_info()

uday = iphone()
uday.total_info()

# COMMAND ----------

# Example 3

# COMMAND ----------

class sports_news:
    def sports_info(self):
        print("sports news")

class political_news:
    def political_info(self):
        print("political news")
        
class movie_news:
    def movie_info(self):
        print("movie news")

class xyz_news:
    def __init__(self):
        self.sports_news= sports_news()
        self.political_news = political_news()
        self.movie_news = movie_news()

    def total_info(self):
        print("Welcome to xyz news")
        self.movie_news.movie_info()
        self.sports_news.sports_info()
        self.political_news.political_info()

ob = xyz_news()
ob.total_info()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Aggregation( HAS- A Relation) Week association
# MAGIC
# MAGIC - Aggregation is a weak form of composition. If you delete the container object contents objects can
# MAGIC - live without container object.

# COMMAND ----------

# MAGIC %md
# MAGIC ### example 1

# COMMAND ----------

class laptop:
    def __init__(self, brand, color, inch):
        self.brand = brand
        self.color = color
        self.inch = inch

    def laptop_info(self):
        print(f'laptop brand : {self.brand}\n color : {self.color}\n inch: {self.inch}')


class emp:
    def __init__(self, ename, eno, lpt):
        self.ename = ename
        self.eno = eno
        self.lpt = lpt

    def emp_info(self):
        print('Emp Name', self.ename)
        print("Emp No ", self.eno)
        print("Emp laptop info :", )
        self.lpt.laptop_info()

laptop1 = laptop("lenovo", "black", 15)
emp1 = emp("sharma", 12121, laptop1)
emp1.emp_info()




# COMMAND ----------

# MAGIC %md
# MAGIC # Inheritance ( IS -A relation)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC - Inheritance is a term that is used to describe a Python class within another class. Classes called subclasses or child    classes can inherit values from parent classes, similar to how children inherit characteristics from their parents in the real world.
# MAGIC
# MAGIC - Inheritance is useful because it allows us to create subclasses that have the same value types as a parent class, without having to declare those types multiple times

# COMMAND ----------

# MAGIC %md
# MAGIC ## Single inheritance

# COMMAND ----------

class parent: # base class, parent class
    
    def house(self):
        print("I have house")

    def car(self):
        print("I have car")

# COMMAND ----------

class child(parent): #Derived class , child class 
    
    def bike(self):
        print("I have Bike")


# COMMAND ----------

ob = child()
ob.house()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Multilevel inheritance

# COMMAND ----------

class test:
    def __init__(self):
        self._a = 10
        
class test1(test):
    def m1(self):
        print(self._a)
    

# COMMAND ----------

ob = test1()
ob.m1()

# COMMAND ----------

class parent: # base class, parent class
    
    def house(self):
        print("I have house")

    def car(self):
        print("I have car")
    
class child(parent): #Derived class , child class 
    
    def bike(self):
        print("I have Bike")
    
class grandchild(child):
    
    def cycle(self):
        print("I have cycle")


# COMMAND ----------

g1 = grandchild()
g1.house()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Hierarchical inheritance

# COMMAND ----------


class parent:

    def house(self):
        print("Iam parent, I have hosue")

class child1(parent):

    def car(self):
        print("Iam child, I have car")

class child2(parent):

    def bike(self):
        print("Iam grand child, I have bike")

ob = child2()
ob.

# COMMAND ----------

# MAGIC %md
# MAGIC ## multiple inheritance

# COMMAND ----------


class father:

    def house(self):
        print("Iam parent, I have hosue")

class mother:

    def car(self):
        print("Iam child, I have car")

class child(father, mother):

    def bike(self):
        print("Iam grand child, I have bike")

ob = child()
ob.

# COMMAND ----------

ccc1 = child()
ccc1.house()

# COMMAND ----------

class parent: # base class, parent class
    
    def __init__(self):
        print("im parent")
        
    def house(self):
        print("I have house")

    def car(self):
        print("I have car")
    
class child(parent): #Derived class , child class 
    
    def __init__(self):
        super().__init__()
        print("im child")
    
    def bike(self):
        print("I have Bike")


# COMMAND ----------

obb = child()

# COMMAND ----------

# MAGIC %md
# MAGIC # Encapsulation

# COMMAND ----------

#public: Public  (generally members declared in a class) are accessible from outside the class.
#protected: The members of a class that are declared protected are only accessible which are deriveved from a base class dit. adding a single underscore ‘_’ symbol before the data member
# private:The members of a class that are declared private are accessible within the class only,
        #private access modifier is the most secure access modifier. adding a double underscore ‘__’ symbol before the data member

# COMMAND ----------

class example:
    def __init__(self):
        self.salary= 10 # public full access
        self._salary1 = 20 # protected accessed by same class and derived class 
        self.__salary2 = 30 # private
        
    def get_private(self):
        return self.__salary2
    
    def set_new_speed(self, new_salary):
        self.__salary2= new_salary
        
e1 = example()
print(e1.salary)
print(e1._salary1)
print(e1.__salary2)




# COMMAND ----------

class customer:
    def __init__(self, n, bankacc, bankbalance):
        self.name = n # public full access
        self._bankacc = bankacc # protected accessed by same class and subclass
        self.__bankbalance= bankbalance # private
        
    def get(self):
        return self.__bankbalance
    
    def set_bankbalance(self, updatedbankbalance):
        self.__bankbalance = updatedbankbalance
    
b1 = customer('john', 12345, 20000)

b1.set_bankbalance(30000)
b1.get()


#print(b1._customer__bankbalance)

# COMMAND ----------

class example:
    def __init__(self):
        self.x= 10
        self._y = 20 
        self.__z = 30
    
    def public_method(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__private_method()
    
    def __private_method(self):
        print(self.x)
    
e2 = example()

e2.public_method()

# COMMAND ----------

# MAGIC %md
# MAGIC # Abstraction

# COMMAND ----------

# MAGIC %md
# MAGIC - By default, Python does not provide abstract classes. Python comes with a module which provides the base for defining Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.

# COMMAND ----------

class parent: 
    
    def add(self):
        pass

    def sub(self):
        pass

class child(parent): 
    
    def __init__(self, n):
        self.num = n
        

p1 = parent()
c1 = child(10)


# COMMAND ----------

# What if i don't want to allow any user to create a object of my parent class
# Methods of parents class sholud be implemented in child class
#The Abstract method is just providing a declaration. The child classes need to provide the definition. 

# COMMAND ----------

#We use Abstraction for hiding the internal details or implementations of a function and showing its functionalities only.
"""
Any class with at least one abstract function is an abstract class. 
In order to create an abstraction class first, you need to import ABC class from abc module. 
This lets you create abstract methods inside it. ABC stands for Abstract Base Class.
from abc import ABC, abstractmethod
"""

#parent is the abstract class that inherits from the ABC class from the abc module.

class parent(ABC): 
    

    def add(self): #concrete method
        pass
    
    
    @abstractmethod
    def sub(self):  #abstract method
        pass

class child(parent): 
    
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
        
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
c1 = child(6,4)
c1.add()

# COMMAND ----------


class parent(ABC): 
    
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass

class child(parent): 
    
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
        
    def add(self):
        return self.num1 + self.num2
        
   
c1 = child(5,6)
c1.add()

# COMMAND ----------

# MAGIC %md
# MAGIC # Polymorphism

# COMMAND ----------

# MAGIC %md
# MAGIC ## operator overloading

# COMMAND ----------

a = 1
b = 2
print(a+b)

# COMMAND ----------

#operator overloading
a = 1
b = 2
print(a + b)

c = "hello"
d = "world"
print(c+d)

e = (1,2,3)
f = (4,5,6)
print(e+f)

# COMMAND ----------

a+b 

# COMMAND ----------

print(int.__add__(a,b))
print(str.__add__(c,d))
print(tuple.__add__(e,f))

# COMMAND ----------

class exp:
    def __init__(self, exp):
        self.exp = exp
    
e1 = exp(1000)
e2 = exp(2000)

print(e1 + e2)

# COMMAND ----------

class exp:
    def __init__(self, exp):
        self.exp = exp
    
    def __add__(self, other):
        return (self.exp + other.exp)
    
e1 = exp(1000)
e2 = exp(2000)

print(e1 + e2)#e1.__add__(e2)

# COMMAND ----------

class expenses:
    def __init__(self, value):r
        self.value = value

    def __add__(self, other):
        return expenses(self.value + other.value)

    def __str__(self):
        return f"{self.value}"
    
    
    
a1 = expenses(10)
a2 = expenses(20)
a3 =expenses(30)
print(a1+a2+a3)


# COMMAND ----------

+ __add__(self, other)
- __sub__(self, other)
* __mul__(self, other)
/  __div__(self, other)
// __floordiv__(self, other)
%  __mod__(self, other)
** __pow__(self, other)
+= __iadd__(self, other)
-=__isub__(self, other)
*=__imul__(self, other)
/=__idiv__(self, other)
//=__ifloordic__(self, other)
**=__ipow__(self, other)
<__lt____(self, other)
<=__le__(self, other)
>__gt__(self, other)

# COMMAND ----------

