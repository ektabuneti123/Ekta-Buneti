#Name - Ekta Buneti
#Roll No- F077
#Q3 D: Write a program for Hierarchical inheritance
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def show_employee(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)


class Manager(Employee):  
    def __init__(self, emp_id, name, department):
        super().__init__(emp_id, name)
        self.department = department

    def show_manager(self):
        self.show_employee()
        print("Department:", self.department)


class Clerk(Employee):    
    def __init__(self, emp_id, name, section):
        super().__init__(emp_id, name)
        self.section = section

    def show_clerk(self):
        self.show_employee()
        print("Section:", self.section)



m = Manager(201, "Rahul", "HR")
c = Clerk(301, "Neha", "Accounts")

m.show_manager()
c.show_clerk()
