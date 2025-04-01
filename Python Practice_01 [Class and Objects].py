# Databricks notebook source
class Mobile:
    charger = "Yes"  #class varible

    def __init__(self,name,color):
        self.name = name #instance variables
        self.color = color #instance variables
    
    def mobile_purchase(self):
        print(f"Thanks for Purchasing {self.color} color {self.name} mobile")

    @classmethod
    def charger_method(cls):
        print(f"Charger is avial in box ? {cls.charger}")

    @staticmethod
    def cost_method(a,b):
        print(a+b)

user1 = Mobile("RedMi","Black")
user1.mobile_purchase()
Mobile.charger_method()  
Mobile.cost_method(1000,2000)


# COMMAND ----------

class Solo_Gym:

    def __init__(self,Name,Age,Height,Weight):
        self.Name = Name
        self.Age = Age
        self.Height = Height
        self.Weight = Weight
    def BMICaluclator(self):
        bmi = self.Weight / (self.Height ** 2)
        return bmi
    
    def body_status(self):
        bmi = self.BMICaluclator()
        if bmi < 18.5:
            return "Underweight - Focus on healthy weight gain"
        elif 18.5 <= bmi < 24.9:
            return "Normal - Maintain your current fitness level"
        elif 25 <= bmi < 29.9:
            return "Overweight - Aim for fat loss and muscle toning"
        else:
            return "Obese - Work on structured weight loss with a proper plan"

    def display_status(self):
        bmi = self.BMICaluclator()
        status = self.body_status()
        print(f"Name: {self.Name}")
        print(f"Weight: {self.Weight} kg, Height: {self.Height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Gym Body Status: {status}")

user = Solo_Gym("ken",26,65,176)

user.display_status()

# COMMAND ----------

