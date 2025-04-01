# Databricks notebook source
# MAGIC %md
# MAGIC # Encapsulation

# COMMAND ----------

class Learner:
    """ Encapsulation """
    def __init__(self, learner_id, name, course, age):
        self.learner_id = learner_id
        self.name = name
        self.course = course
        self._age = age

# COMMAND ----------

kanth_learner = Learner("BCT123", "Kanth","DSCT",25)

# COMMAND ----------

kanth_learner.name

# COMMAND ----------

kanth_learner.age

# COMMAND ----------

kanth_learner._age

# COMMAND ----------

# MAGIC %md
# MAGIC # Name Mangling

# COMMAND ----------

# MAGIC %md
# MAGIC Process by which name of the attribute is modified

# COMMAND ----------

class Learner1:
    """
    Restrict Access helps us to prevent the direct access to the
    attributes in order to avoid making problematic changes
    
    """
    def __init__(self, learner_id, name, course, age):
        self.learner_id = learner_id
        self.name = name
        self.course = course
        self.__age = age

# COMMAND ----------

kanth_learner = Learner1("BCT123", "Kanth","DSCT",25)

# COMMAND ----------

kanth_learner.name

# COMMAND ----------

kanth_learner.__age

# COMMAND ----------

kanth_learner._age

# COMMAND ----------

kanth_learner._Learner1__age

# COMMAND ----------

# MAGIC %md
# MAGIC # Getter, Setter & Property

# COMMAND ----------

class Salary:
    
    def __init__(self, salary):
        self._salary = salary
        
    def get_salary(self):
        return self._salary
    
    def set_salary(self, new_salary):
        if isinstance(new_salary, float) and new_salary > 0:
            self._salary = new_salary
            
        else:
            print("Enter Valid Salary")

# COMMAND ----------

kanth_salary = Salary(20000)

# COMMAND ----------

kanth_salary.salary

# COMMAND ----------

kanth_salary.get_salary()

# COMMAND ----------

kanth_salary.set_salary(15000.5)

# COMMAND ----------

kanth_salary.get_salary()

# COMMAND ----------

class Salary:
    
    def __init__(self, salary):
        self._salary = salary
        
    @property
    def salary(self):
        print("Executing Getter")
        return self._salary
    
    @salary.setter
    
    def salary(self, new_salary):
        print("Executing Setter")
        if isinstance(new_salary, float) and new_salary > 0:
            self._salary = new_salary
            
        else:
            print("Enter Valid Salary")

# COMMAND ----------

kanth_salary = Salary(20000)

# COMMAND ----------

kanth_salary.salary

# COMMAND ----------

kanth_salary.salary = 15500.0

# COMMAND ----------

kanth_salary.salary

# COMMAND ----------

# MAGIC %md
# MAGIC # Aggregation vs Composition

# COMMAND ----------

# MAGIC %md
# MAGIC Aggregation: Aggregation is a "has a" relationship. An instance of class B 
# MAGIC has an instance of Class A but they can exist independently
# MAGIC
# MAGIC Composition: A composed object cannot exist without the object that contains it.

# COMMAND ----------

class BmiCalc():
    
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        
    def bmi(self):
        BMI = self.weight/(self.height*self.height)
        if BMI <=18.5:
            print("Underweight")
        elif BMI >18.5 and BMI < 24.99:
            print("Normal Weight")
        elif BMI > 25 and BMI < 29.99:
            print("Over Weight")
        else:
            print("BMI Calculated", BMI )
            print("Obesity")
            
class GymMember:
    
    def __init__(self,name, mbmi):
        self.name = name
        self.mbmi = mbmi
    
    def show_bmi(self):
        self.mbmi.bmi()

# COMMAND ----------

mem_bmi = BmiCalc(79, 1.89)

# COMMAND ----------

kanth = GymMember("Kanth",mem_bmi)

# COMMAND ----------

kanth.show_bmi()

# COMMAND ----------

# MAGIC %md
# MAGIC # Inheritance

# COMMAND ----------

class BankEmi():
    
    def __init__(self, salary, emi):
        self.salary = salary
        self.emi = emi
    
    def apcheck(self):
        if self.salary > self.emi:
            print("Loan can be approved")
        else:
            print("Loan cannot be approved")
            
            
class AnotherBank(BankEmi):
    pass

# COMMAND ----------

xbank = AnotherBank(10000,5000)

# COMMAND ----------

xbank.apcheck()

# COMMAND ----------

class BankEmi():
    
    def __init__(self, salary, emi):
        self.salary = salary
        self.emi = emi
    
    def apcheck(self):
        if self.salary > self.emi:
            print("Loan can be approved")
        else:
            print("Loan cannot be approved")
            
            
class AnotherBank(BankEmi):
    
    def __init__(self, cibil, loan):
        self.cibil = cibil
        self.loan = loan

# COMMAND ----------

ybank = AnotherBank(800,1000000)

# COMMAND ----------

ybank.cibil

# COMMAND ----------

ybank.salary

# COMMAND ----------

# MAGIC %md
# MAGIC If the Subclasss has its own __init__() method, the attributes
# MAGIC of the superclass are not inherited automatically

# COMMAND ----------

class BankEmi():
    
    def __init__(self, salary, emi):
        self.salary = salary
        self.emi = emi
    
    def apcheck(self):
        if self.salary > self.emi:
            print("Loan can be approved")
        else:
            print("Loan cannot be approved")
            
            
class AnotherBank(BankEmi):
    
    def __init__(self, cibil, loan, salary, emi):
        BankEmi.__init__(self, salary, emi)
        self.cibil = cibil
        self.loan = loan

# COMMAND ----------

ybank = AnotherBank(800,100000, 30000, 20000)

# COMMAND ----------

ybank.salary

# COMMAND ----------

ybank.emi

# COMMAND ----------

ybank.cibil

# COMMAND ----------

ybank.loan

# COMMAND ----------

class BankEmi():
    
    def __init__(self, salary, emi):
        self.salary = salary
        self.emi = emi
    
    def apcheck(self):
        if self.salary > self.emi:
            print("Loan can be approved")
        else:
            print("Loan cannot be approved")
            
            
class AnotherBank(BankEmi):
    
    def __init__(self, cibil, loan, salary, emi):
        super().__init__(salary, emi)
        self.cibil = cibil
        self.loan = loan

# COMMAND ----------

ybank = AnotherBank(800,100000, 30000, 20000)

# COMMAND ----------

ybank.salary

# COMMAND ----------

ybank.emi

# COMMAND ----------

class BankEmi():
    
    def __init__(self, salary, emi):
        self.salary = salary
        self.emi = emi
    
    def apcheck(self):
        if self.salary > self.emi:
            print("Loan can be approved")
        else:
            print("Loan cannot be approved")
            
            
class AnotherBank(BankEmi):
    
    def __init__(self, cibil, loan, salary, emi):
        super().__init__(salary, emi)
        self.cibil = cibil
        self.loan = loan
        
    def elig(self):
        if self.cibil > 650 and self.loan < 150000:
            print("Loan Approved")
        else:
            print("Loan Rejected")

# COMMAND ----------

ybank = AnotherBank(500,100000, 30000, 20000)

# COMMAND ----------

ybank.apcheck()

# COMMAND ----------

ybank.elig()

# COMMAND ----------

# MAGIC %md
# MAGIC # Method Overriding

# COMMAND ----------

# MAGIC %md
# MAGIC Method Overriding: Method overriding is an ability of any object-oriented 
# MAGIC programming language that allows a subclass or child class to provide a 
# MAGIC specific implementation of a method that is already provided by one of 
# MAGIC its super-classes or parent classes. 
# MAGIC
# MAGIC Method Overloading: Two methods in the same class have the same name but different parameters, so when you call the method, the version that is executed is determined by the data types of the arguments or by the number of arguments

# COMMAND ----------

class BepecCt:
    
    def __init__(self):
        self.topics = []
        
    def add_lectures(self, session):
        print(f"Adding {session.capitalize()} lecture to the Dashboard")
        self.topics.append(session)
        print(f"{session.capitalize()} was added into the Dashboard.")
              


class KanthCt(BepecCt):
              
    def add_lectures(self, session):
        print("Notification! Your Dashboard got Unlocked with New Lecture")
        BepecCt.add_lectures(self,session)
        print("List of Sessions:", self.topics)
              
              
              
    

# COMMAND ----------

dslectures = KanthCt()

# COMMAND ----------

dslectures.add_lectures("Python")

# COMMAND ----------

dslectures.add_lectures("OOPS")

# COMMAND ----------

dslectures.add_lectures("Tableau")

# COMMAND ----------

# MAGIC %md
# MAGIC # Polymorphism

# COMMAND ----------

class File:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension
        
    def open():
        print("Opening a regular file")
        
class PdfFile(File):
    
    def __init__(self, name):
        super().__init__(name, ".pdf")
    
        
    def open(self):
        print("Opening a PDF file")
        
class TextFile(File):
    
    def __init__(self,name):
        super().__init__(name, ".txt")
        
    def open(self):
        print("Opening a Text File")


# COMMAND ----------

pdf1 = PdfFile("OOPS")

# COMMAND ----------

pdf1.open()

# COMMAND ----------

text1 = TextFile("Polymorphism")

# COMMAND ----------

text1.open()

# COMMAND ----------

