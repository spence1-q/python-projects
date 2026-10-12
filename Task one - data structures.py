#  Create a list named marks containing five subject marks
marks = [78, 85, 90, 72, 88]

#  Display all the marks
print("Original Marks:", marks)

#  Calculate and display the total marks using sum()
total = sum(marks)
print("Total Marks:", total)

#  Calculate and display the average mark
average = total / len(marks)
print("Average Mark:", average)

#  Display the highest mark using max()
print("Highest Mark:", max(marks))

#  Display the lowest mark using min()
print("Lowest Mark:", min(marks))

#  Modify the mark of the third subject and display the updated list
marks[2] = 95  
print("Updated Marks List:", marks)
