# 1. Create a base class called Person
class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    # 2. Define display_details() method in Person class
    def display_details(self):
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# 3. Create a derived class called Student that inherits from Person
class Student(Person):
    def __init__(self, person_id, name, age, course, marks):
        super().__init__(person_id, name, age)
        self.course = course
        self.marks = marks

    # 4. Define calculate_grade() method in Student class
    def calculate_grade(self):
        if self.marks >= 70:
            return "Grade A"
        elif self.marks >= 60:
            return "Grade B"
        elif self.marks >= 50:
            return "Grade C"
        else:
            return "Grade D"

    # 5. Override display_details() method using super()
    def display_details(self):
        super().display_details()
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")


# 6. Create another derived class called Lecturer that inherits from Person
class Lecturer(Person):
    def __init__(self, person_id, name, age, department, monthly_salary):
        super().__init__(person_id, name, age)
        self.department = department
        self.monthly_salary = monthly_salary

    # 7. Define calculate_annual_salary() method in Lecturer class
    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    # 8. Override display_details() method using super()
    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
        print(f"Monthly Salary: {self.monthly_salary:,.2f}")
        print(f"Annual Salary: {self.calculate_annual_salary():,.2f}")


# 9. Create one Student object and one Lecturer object using sample data
student_obj = Student(person_id="S-05-0001/2024", name="Obed Ondieki", age=26, course="Software Engineering", marks=76)
lecturer_obj = Lecturer(person_id="M-300", name="Dr. Mercy", age=42, department="Information Technology", monthly_salary=95000)

# 10. Display details and call respective methods
print("=" * 30)
print("STUDENT DETAILS")
print("=" * 30)
student_obj.display_details()

print("\n" + "=" * 30)
print("LECTURER DETAILS")
print("=" * 30)
lecturer_obj.display_details()
