# Programmer: Mai Lillie
# Date: 11/8/24
# Program #4 Employee Class:

# Creates our class with employee characteristics
class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
    def get_name(self):
        return self.name
    def get_id_number(self):
        return self.id_number
    def get_department(self):
        return self.department
    def get_job_title(self):
        return self.job_title

# Creates our employees
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
# Loops to print their information
x = 1
while x <= 3:
    if x == 1:
        employee_ex = employee1
    elif x == 2:
        employee_ex = employee2
    elif x == 3:
        employee_ex = employee3
    name = employee_ex.get_name()
    id_number = employee_ex.get_id_number()
    department = employee_ex.get_department()
    job_title = employee_ex.get_job_title()
    print(f"Name: {name} \nId Number: {id_number} \nDepartment: {department} \nJob Title: {job_title}")
    x += 1

