class Employee:
    def __init__(self, name):
        self.name = name

    def salary(self):
        print("Salary not defined")


class RegularEmployee(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name)
        self.salary_amount = salary

    def salary(self):
        print(self.name, "Salary:", self.salary_amount)


class ContractEmployee(Employee):
    def __init__(self, name, hours, rate):
        Employee.__init__(self, name)
        self.hours = hours
        self.rate = rate

    def salary(self):
        print(self.name, "Salary:", self.hours * self.rate)


# Example
e1 = RegularEmployee("Ram", 30000)
e2 = ContractEmployee("Sam", 100, 200)

e1.salary()
e2.salary()