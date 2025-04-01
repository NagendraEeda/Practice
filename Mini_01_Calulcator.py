# Databricks notebook source
# Calculator Class

class Functions:

    def __init__(self, *num):
        self.num = num
        print("Welcome to the Calculator Program!")

    def add(self):
        total = 0
        for i in self.num:
            total += i
        return total

    def sub(self):
        total = self.num[0]
        for i in self.num[1:]:
            total -= i
        return total
    
    def mul(self):
        total = self.num[0]
        for i in self.num[1:]:
            total *= i
        return total

    def div(self):
        total = self.num[0]
        for i in self.num[1:]:
            if i != 0:
                total /= i
            else:
                return "Error! Division by zero."
        return total


# Subclass to Handle User Interaction
class Calculator(Functions):

    def menu(self):
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        while True:
            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice == 5:
                    print("Exiting the program. Goodbye!")
                    break

                # Input numbers from the user
                nums = tuple(map(float, input("Enter the numbers separated by spaces: ").split()))
                calc = Functions(*nums)

                if choice == 1:
                    print(f"The result of addition is: {calc.add()}")
                elif choice == 2:
                    print(f"The result of subtraction is: {calc.sub()}")
                elif choice == 3:
                    print(f"The result of multiplication is: {calc.mul()}")
                elif choice == 4:
                    print(f"The result of division is: {calc.div()}")
                else:
                    print("Invalid choice! Please choose between 1 and 5.")

            except ValueError:
                print("Invalid input! Please enter numeric values.")

# Main Program Execution
if __name__ == "__main__":
    calc_app = Calculator()
    calc_app.menu()


# COMMAND ----------

class calsi:

    num1 = int(input("Enter the first value : "))
    num2 = int(input("Enter the Second Value : "))

    operation = input("Choose the operation [+,-,*,/,%] : ")

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return lamda num1,num2 : num1 operation num2