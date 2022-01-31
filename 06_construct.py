class employee:
    company='Google'

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")

    def getinfo(self):
        print(f"The Name of the Employee is {self.name}")
        print(f"The Subunit of the Employee is {self.subunit}")
    
    def getSalary(self,signature):
        print(f"Salary for this Employee Working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("Good Morning ,Bikash Sir")
    
    @staticmethod
    def time():
        print("The Time is 9AM in the Morning")

bicky=employee('Bicky',10000,'Youtube')
bicky.getinfo()
bicky.getSalary('Bikash')
bicky.greet()
bicky.time()