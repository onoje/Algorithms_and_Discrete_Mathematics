employee_list = []
threshold = 70000

class Employee:
    def _init_(self,name,age,position,salary,department):
        self.name=name
        self.age=age
        self.position=position
        self.salary=salary
        self.department=department

def is_manager(employee):
    if employee.position == "Manager":
        return(True)
    else:
        return(False)
def is_high_earner(employee, threshold):
    if employee.salary > threshold:
        return(True)
    else:
        return(False)

def works_in_department(employee, department_name):
    if employee.department == department_name:
        return(True)
    else:
        return(False)

def add_employee(employee_list, employee):
        employee_list.append(employee)

def remove_employee(employee_list, name):
    for emp in employee_list:
        if emp.name == name:
            employee_list.remove(emp)
            return 

def query_employees(employee_list, predicate, *args):
    return [emp for emp in employee_list if predicate(emp, *args)]


employees = []
add_employee(employees,Employee("Alice",30,"Manager",80000,"HR"))
add_employee(employees,Employee("Bob",25,"Developer",60000,"IT"))

high_earners=query_employees(employees,is_high_earner,70000)
print([emp.name for emp in high_earners])