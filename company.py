from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employees: ")
        for i in self.employees:
            print(i.fname, i.lname)
        print("-------------------")

    def pay_employees(self):
        print("Paying Employees")
        for i in self.employees:
            print("Paycheck for:", i.fname)
            print(f"Amount: ${i.calc_paycheck():,.2f}")
        print("-------------------")


def main():
    my_company = Company()

    employee1 = SalaryEmployee('Sarah','Henry',50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Bruce','Wayne',25,50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Peter','Parker',10000,50,15)
    my_company.add_employee(employee3)
    

    my_company.display_employees()
    my_company.pay_employees()

main()