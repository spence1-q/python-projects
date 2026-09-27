# Define a function named calculate_grade(mark) that accepts the student's mark as a parameter
def calculate_grade(mark):
    # The grading criteria and return the appropriate grade
    if 70 <= mark <= 100:
        return 'A'
    elif 60 <= mark <= 69:
        return 'B'
    elif 50 <= mark <= 59:
        return 'C'
    elif 40 <= mark <= 49:
        return 'D'
    elif 0 <= mark < 40:
        return 'F'
    else:
        return "Invalid mark! Please enter a value between 0 and 100."

def main():
    print("--- University Grading System ---")
    
    # User to enter a student's mark[cite: 1]
    try:
        student_mark = float(input("Enter the student's mark: "))
        
        # vi. Call the function and display the returned grade[cite: 1]
        result_grade = calculate_grade(student_mark)
        print(f"---------------------------------")
        print(f"Student Mark:  {student_mark}")
        print(f"Assigned Grade: {result_grade}")
        print(f"---------------------------------")
        
    except ValueError:
        print("Invalid input. Please enter a numerical value for the mark.")

# Execute the program
if __name__ == "__main__":
    main()
