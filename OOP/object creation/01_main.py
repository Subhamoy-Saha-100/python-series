class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is not there")
harry = Employee()

harry.name = "Harry"
harry.salary = "50k"
# print(harry.company)
Employee.company = "Youtube"
# print(harry.company)
# print(harry.name)
# print(harry.salary)
print(harry.getSalary())