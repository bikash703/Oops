number =int(input("Enter a Number :"))

class Calculator:
    def __init__(self,number):
        self.number=number
    
    def square(self):
        print(f"The square value of {self.number} is {self.number **2}")

    def squareRoot(self):
        print(f"The square value of {self.number} is {self.number **0.5}")
    
    def cube(self):
        print(f"The square value of {self.number} is {self.number **3}")

    @staticmethod
    def greet():
        print("Hello ,Good Morning")

num=Calculator(number)
num.square()
num.squareRoot()
num.cube()
num.greet()

