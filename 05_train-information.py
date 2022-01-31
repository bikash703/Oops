class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def status(self):
        print(f"The Name of the Train is {self.name}")
        print(f"The Availabe seats of the Train is {self.seats}")
    
    def fareinfo(self):
        print(f"The Amount of the Ticket is Rs {self.fare}")
    
    def bookticket(self):
        if self.seats > 0:
            print(f"Your ticket has been Booked. Your ticket Number is {self.seats}\n")
            self.seats=self.seats - 1
        else:
            print("Sorry!,This Train is fulled!\n ")
        
    def cancelticket(self):
        pass

a=Train("indian Railway",80,10)
a.status()
a.fareinfo()
a.bookticket()
a.bookticket()
a.bookticket()
a.status()
