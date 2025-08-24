class Employee:
    def __init__(self, name, baseSalary):
        self.name = name
        self.baseSalary = float(baseSalary)
        
    def calcBonus(self):
        return self.baseSalary * 0.10

class Manager(Employee):
    def calcBonus(self):
        return self.baseSalary * 0.30
    
class Seller(Employee):
    def calcBonus(self):
        bonus = super().calcBonus()
        return bonus + 200
    

manager = Manager(name="Luis", baseSalary=10000)
seller = Seller(name="Dalton", baseSalary=8000)    

employeeList = [manager, seller]

for employee in employeeList:
    print(f"The employee {employee.name} recieved a bonus of ${employee.calcBonus()}")
    
manager2 = Manager(name = input("Manager name: "), baseSalary=input("Its base salary: "))
seller2 = Seller(name = input("Seller name: "), baseSalary=input("Its base salary: "))

manager2.calcBonus()
seller2.calcBonus()

print(f"The manager {manager.name} recieved a bonus of {manager.calcBonus()}")
print(f"The seller {seller.name} recieved a bonus of {seller.calcBonus()}")