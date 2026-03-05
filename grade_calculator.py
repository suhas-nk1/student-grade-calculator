name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 50:
    grade = "D"

else:
    grade = "Fail"

print("Student:", name)
print("Marks:", marks)
print("Grade:", grade)
