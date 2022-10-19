""" required modules"""
import secrets


class Employee(object):
    """initializing all the data member of employee that will store necessary details"""

    def __init__(self):
        self.__emp_id = None
        self.__name = None
        self.__email = None
        self.__mob_num = None
        self.__department = None
        self.__address = None
        self.__salary = None

    """setters for the data members for setting up the data"""

    def set_emp_id(self, emp):
        if self.__emp_id is None:
            self.__emp_id = emp
            print("Employee id is set")
        else:
            print("Already set")

    def set_emp_name(self, name):
        if self.__name is None:
            self.__name = name
            print("Employee name is set")
        else:
            print("Already set")

    def set_emp_email(self, email):
        if self.__email is None:
            self.__email = email
            print("Employee email is set")
        else:
            print("Already set")

    def set_mob_num(self, mob_num):
        if self.__mob_num is None:
            self.__mob_num = mob_num
            print("Employee Mobile number is set")
        else:
            print("Already set")

    def set_department(self, department):
        if self.__department is None:
            self.__department = department
            print("Department of the Employee is set")
        else:
            print("Already set")

    def set_address(self, address):
        if self.__address is None:
            self.__address = address
            print("Employee Address is set")
        else:
            print("Already set")

    def set_salary(self, salary):
        if self.__salary is None:
            self.__salary = salary
            print("Employee Salary is set")
        else:
            print("Already set")

    """method for updating the data member"""

    def update_emp_id(self, emp):
        if self.__emp_id is None:
            print("Can't Update")
        else:
            self.__emp_id = emp
            print("Employee is updated")

    def update_emp_name(self, name):
        if self.__name is None:
            print("Can't Update")
        else:
            self.__name = name
            print("Employee name is updated")

    def update_emp_email(self, email):
        if self.__email is None:
            print("Can't Update")
        else:
            self.__email = email
            print("Employee email is updated")

    def update_mob_num(self, mob_num):
        if self.__mob_num is None:
            print("Can't Update")
        else:
            self.__mob_num = mob_num
            print("Employee Mobile number is updated")

    def update_department(self, department):
        if self.__department is None:
            print("Can't Update")
        else:
            self.__department = department
            print("Department of the Employee is updated")

    def update_address(self, address):
        if self.__address is None:
            print("Can't Update")
        else:
            self.__address = address
            print("Employee Address is updated")

    def update_salary(self, salary):
        if self.__salary is None:
            print("Can't Update")
        else:
            self.__salary = salary
            print("Employee Salary is updated")

    """getters for the data member for getting the data"""

    def get_emp_id(self):
        if self.__emp_id is None:
            return "not set"
        return self.__emp_id

    def get_emp_name(self):
        if self.__name is None:
            return "not set"
        return self.__name

    def get_emp_email(self):
        if self.__email is None:
            return "not set"
        return self.__email

    def get_mob_num(self):
        if self.__mob_num is None:
            return "not set"
        return self.__mob_num

    def get_department(self):
        if self.__department is None:
            return None
        return self.__department

    def get_address(self):
        if self.__address is None:
            return "not set"
        return self.__address

    def get_salary(self):
        if self.__salary is None:
            return None
        return self.__salary

    def create_emp(self, directory):
        new_emp_id = secrets.randbelow(1000000000)
        print(f"your employee id is {new_emp_id}")
        if directory.get(new_emp_id) is None:
            emp.set_emp_id(new_emp_id)
            print("Enter Name:-")
            emp_name = input()
            print("Enter Email:-")
            emp_email = input()
            print("Enter Mobile Number")
            emp_mob_num = input()
            print("Enter Address")
            emp_address = input()
            # emp.set_emp_id(new_emp_id)
            emp.set_emp_name(emp_name)
            emp.set_emp_email(emp_email)
            emp.set_address(emp_address)
            emp.set_mob_num(emp_mob_num)
            directory[new_emp_id] = self
        else:
            print("cannot create employee records")

    @staticmethod
    def get_information(directory):
        print("Enter employee id")
        searched_emp_id = int(input())
        if directory.get(searched_emp_id) is None:
            print("employee id doesn't exists")
        else:
            searched_emp = directory[searched_emp_id]
            searched_name = searched_emp.get_emp_name()
            searched_email = searched_emp.get_emp_email()
            searched_mob_num = searched_emp.get_mob_num()
            searched_address = searched_emp.get_address()
            searched_department = searched_emp.get_department()
            searched_salary = searched_emp.get_salary()
            print(f"Employee id:- {searched_emp_id}")
            print(f"Name:- {searched_name}")
            print(f"Email:- {searched_email}")
            print(f"Mobile Number:- {searched_mob_num}")
            print(f"Address:- {searched_address}")
            if searched_department is not None:
                print(f"Department:- {searched_department}")
            if searched_salary is not None:
                print(f"salary:- {searched_salary}")

    @staticmethod
    def update_information(directory):
        print("Enter employee id")
        queried_emp_id = int(input())
        if directory.get(queried_emp_id) is None:
            print("employee id doesn't exists")
        else:
            queried_emp = directory[queried_emp_id]
            print("select from the option given below to update the information")
            while True:
                print("1:name 2:email 3:Mobile number 4:address 0:go to main menu")
                update_option = int(input())
                if update_option == 0:
                    break
                elif update_option == 1:
                    print("enter the new name")
                    name = input()
                    queried_emp.update_emp_name(name)
                elif update_option == 2:
                    print("enter the new email")
                    email = input()
                    queried_emp.update_emp_email(email)
                elif update_option == 3:
                    print("enter the new mobile number")
                    mob_num = int(input())
                    queried_emp.update_mob_num(mob_num)
                elif update_option == 4:
                    print("enter address")
                    address = input()
                    queried_emp.update_address(address)

    def remove(self):
        self.__emp_id = None
        self.__name = None
        self.__email = None
        self.__mob_num = None
        self.__department = None
        self.__address = None
        self.__salary = None

    @staticmethod
    def remove_emp(directory):
        print("Enter employee id")
        emp_id_to_delete = int(input())
        if directory.get(emp_id_to_delete) is None:
            print("employee id doesn't exists")
        else:
            emp_to_delete = directory[emp_id_to_delete]
            emp_to_delete.remove()
            directory.pop(emp_id_to_delete)
            print("employee records deleted")
        # print("deleted")

    @staticmethod
    def admin(directory):
        print("Enter employee id")
        emp_id = int(input())
        if directory.get(emp_id) is None:
            print("employee id doesn't exists")
        else:
            emp = directory[emp_id]
            while True:
                print("Select the option to set")
                print("1:set salary 2:set Department 3:update salary 4:update department 5:All Employees 0:main menu")
                admin_option = int(input())
                if admin_option == 0:
                    break
                elif admin_option == 1:
                    print("enter salary")
                    salary = int(input())
                    emp.set_salary(salary)
                elif admin_option == 2:
                    print("enter department")
                    department = input()
                    emp.set_department(department)
                elif admin_option == 3:
                    print("enter salary")
                    salary = int(input())
                    emp.update_salary(salary)
                elif admin_option == 4:
                    print("enter department")
                    department = input()
                    emp.update_department(department)


if __name__ == "__main__":
    Directory = {}
    while True:
        print("1:New Employee 2:Get Information 3:Update Information 4:Delete Employee 5:admin 0:Exit")
        option = int(input())
        if option == 0:
            exit()
        elif option == 1:
            emp = Employee()
            emp.create_emp(Directory)
        elif option == 2:
            Employee.get_information(Directory)
        elif option == 3:
            Employee.update_information(Directory)
        elif option == 4:
            Employee.remove_emp(Directory)
        elif option == 5:
            print(f"_________Admin________")
            Employee.admin(Directory)
