from main import Student

try:
    student1_name = input("Enter your name \n")
    student2_id = input("Enter your ID \n")
    student3_class = input("Enter your class \n")
    Student.create(student_name=student1_name, student_id=student2_id, student_class=student3_class)
    print("Student created successfully")


except:
    print("Failed to create student, use a different id")
