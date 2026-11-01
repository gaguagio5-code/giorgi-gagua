class Employee:
    def __init__ (self, name,  salary):
        self.name = name
        self.salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def salary(self):
        return self.__salary    

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("The salary must be positive.")
        self.__salary = value

    @salary.deleter
    def salary(self):
        print(f"{self.salary} is deleted")
        del self.__salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        print(f"Manager Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

Manager = Manager("John Doe", 80000, "IT") # type: ignore
try:
    print(Manager.salary)
except AttributeError as e:
    print(f"Error: {e}")

print([attr for attr in dir(Manager) if "salary" in attr])
print(f"property-ით: {Manager.salary}")

print()
Manager.get_info() # type: ignore
Manager.salary = 90000
print(f"Updated Salary: {Manager.salary}")

try:
    Manager.salary = -1000
except ValueError as e:
    print(f"Error: {e}")

del Manager.salary
try:
    print(Manager.salary)
except AttributeError as e:
    print(f"Error: {e}")