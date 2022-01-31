class Programmer:
    company='Microsoft'
    
    def __init__(self, name, salary, product):
        self.name = name
        self.product = product
        self.salary = salary
    
    def get_info(self):
        print(f'The Name of the {self.company} programmer is {self.name} , product is {self.product} and salary is {self.salary}')

Bicky=Programmer("Bicky",10000,"skype")
Racky=Programmer("Racky",15000,"gthub")
Bicky.get_info()
Racky.get_info()

