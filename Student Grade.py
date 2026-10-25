class Student:
    def __init__(self):
        self.student_name = ""
        self.registration_number = ""
        self.course = ""
        self.mark = 0.0

    def setStudentDetails(self, name, reg_no, course, mark):
        self.student_name = name
        self.registration_number = reg_no
        self.course = course
        self.mark = mark

    def calculateGrade(self):
        if 70 <= self.mark <= 100:
            return 'A'
        elif 60 <= self.mark <= 69:
            return 'B'
        elif 50 <= self.mark <= 59:
            return 'C'
        elif 40 <= self.mark <= 49:
            return 'D'
        elif self.mark < 40:
            return 'F'
        else:
            return 'Invalid Mark'

    def displayStudentDetails(self):
        grade = self.calculateGrade()
        print("\n--- Student Details ---")
        print(f"Student Name       : {self.student_name}")
        print(f"Registration Number: {self.registration_number}")
        print(f"Course             : {self.course}")
        print(f"Mark               : {self.mark}")
        print(f"Grade              : {grade}")

# Main
if __name__ == "__main__":
    # Create a Student object
    student = Student()
    
    # Set the student's details
    student.setStudentDetails("Obed Ondieki", "Bscit-01/100/2025", "Software Engineering", 78.0)
    
    # Calculate the grade and display the student details and grade
    student.displayStudentDetails()
