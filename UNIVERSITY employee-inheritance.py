# i. Create a parent class named Employee
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    # ii. Include a method named displayEmployee() to display the employee details
    def displayEmployee(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


# iii. & iv. Create a child class named Lecturer that inherits from Employee and adds teaching subject
class Lecturer(Employee):
    def __init__(self, name, employee_id, teaching_subject):
        super().__init__(name, employee_id)
        self.teaching_subject = teaching_subject

    # v. Include a method named displayLecturer() to display employee name, ID, and teaching subject
    def displayLecturer(self):
        super().displayEmployee()
        print(f"Teaching Subject: {self.teaching_subject}")


# vi. In the main section:
if __name__ == "__main__":
    # Create a Lecturer object and assign details/teaching subject
    lecturer = Lecturer(name="Newton Nyaribo", employee_id="EMP-405", teaching_subject="Database Management Systems")
    
    # Display all information
    print("--- Lecturer Details ---")
    lecturer.displayLecturer()
