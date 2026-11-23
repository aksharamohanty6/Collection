print("==============Welcome to the Student Data Organizer!==============")

print("Select an option:")

print("1. Add Student")
print("2. Display All Students")
print("3. Update Student Information")
print("4. Delete Student")
print("5. Display Subjects Offered")
print("6. Exit")

choice = input("Enter your choice: ")

if choice == "1":

    print("Enter Student Details:")
    
    student_id = input("Student ID: ")
    student_name = input("Name: ")
    student_age = input("Age: ")
    student_grade = input("Grade: ")
    student_dob = input("Date of Birth (YYYY-MM-DD): ")
    student_subjects = input("Subjects (comma-separated): ").split(',')

    print("Student added successfully!")

print("Select an option:")

print("1. Add Student")
print("2. Display All Students")
print("...")

choice = input("Enter your choice: ")
if choice == "2":
    print("-----Displaying All Students-----")

    student = f"ID: {student_id}, Name: {student_name}, Age: {student_age}, Grade: {student_grade}, DOB: {student_dob}, Subjects: {', '.join(student_subjects)}"
    print(student)
    print("...")

    print("Select an option:")
    print("...")

    
