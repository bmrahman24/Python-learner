marks = input("Please enter ur marks: ")
marks = int (marks)

if marks >= 81:
    grade = "A+"
elif marks >= 69:
    grade = "A"
elif marks >= 59:
    grade = "A-"
elif marks >= 49:
    grade = "B"
else:
    grade = "F"
    
print (" Your grade is", grade)

