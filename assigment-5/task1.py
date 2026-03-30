# Task 1: Create a Dictionary of Student Marks
import pickle

"""
# I am doing this task after completing uptill Module 11
# So, I know the usage of pickle module 

# student marks dictionary
student_marks = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90, "Eve": 88}

# dump the marks into a file
with open("student_marks", "wb") as file:
    pickle.dump(student_marks, file)
"""

# read marks from the file
with open("student_marks", "rb") as file:
    student_marks = pickle.load(file)

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
