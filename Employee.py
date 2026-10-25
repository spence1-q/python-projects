class Employee:
    #  Define attributes and initialize using __init__ constructor
    def __init__(self, employee_id, name, basic_salary, overtime_hours):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary
        self.overtime_hours = overtime_hours

    # Calculate and return gross salary
    def calculate_gross_salary(self):
        return self.basic_salary + (self.overtime_hours * 500)

    # Calculate and return tax (10% of gross salary)
    def calculate_tax(self):
        return self.calculate_gross_salary() * 0.10

    # Calculate and return net salary
    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        tax = self.calculate_tax()
        return gross - tax


# employee objects and display details
emp1 = Employee("EMP101", "Alice", 50000, 10)
emp2 = Employee("EMP102", "Brian", 65000, 6)

employees = [emp1, emp2]

for emp in employees:
    print(f"--- Payroll Summary for {emp.name} ({emp.employee_id}) ---")
    print(f"Gross Salary : KSh {emp.calculate_gross_salary():,.2f}")
    print(f"Tax Deducted : KSh {emp.calculate_tax():,.2f}")
    print(f"Net Salary   : KSh {emp.calculate_net_salary():,.2f}\n")
