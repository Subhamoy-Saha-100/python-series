class Employee: # Base class
    def __init__(self,name):
        self.name = name

class Programmer(Employee): # Derived or child class
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        
