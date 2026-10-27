students = []

def add_student():
    admin_password = "admin123"
    password = input("Enter admin password: ")
    if password != admin_password:
        print("Incorrect password. Access denied.")
        return     
    else:
       print("Access granted. You can add a student.")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Marks:", student["marks"])

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")

