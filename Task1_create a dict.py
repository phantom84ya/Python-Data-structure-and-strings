student_marks = {"Alice":85,"Bob":34,"Will":64}
student_name = input("enter the student's name:")

if student_name in student_marks :
    print(f"{student_name} marks: {student_marks[student_name]}")
else:
    print("student not found")