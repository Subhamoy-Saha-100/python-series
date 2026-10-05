class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def getSalary(self):
        if(not self.salary):
            print("No salary just beacuse of lala company")
        else:
            print(f"Name: {self.name} \nSalary is : {self.salary}")

harry = Employee("Harry",135540)

print(harry.getSalary())