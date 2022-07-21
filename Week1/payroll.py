class Employee:
    def __init__(self, first, last, empid, hpay):
        self.fname = first
        self.lname = last
        self.empid = empid
        self.hpay = hpay
        
    def setFirst(self, first):
        self.fname = first
        
    def setLast(self, last):
        self.lname = last
        
    def setEmpId(self, empid):
        self.empid = empid
        
    def setHPay(self, hpay):
        self.hpay = hpay
        
    def getFirst(self):
        return self.fname
    
    def getLast(self):
        return self.lname
    
    def getEmpId(self):
        return self.empid
    
    def getHPay(self):
        return self.hpay
        
    def pay(self, totalhrs):
        if totalhrs <= 40:
            return self.hpay * totalhrs
        else:
            return float(40 * self.hpay + ((totalhrs - 40 )* (self.hpay * 1.5)))
        
ID = input("Please enter the Employee's ID: ")
fname = input("Please enter the Employee's First Name: ")
lname = input("Please enter the Employee's Last Name: ")
hrspay = float(input("Please enter the Employee's Hourly Pay Rate: "))
hrs = float(input("How many hours did {fname} work this week? "))
    
employee = Employee(ID, fname, lname, hrspay) 
print(f" {fname} {lname}'s  paycheck amount is: ${employee.pay(hrs):.2f}")