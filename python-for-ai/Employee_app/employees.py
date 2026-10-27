
Employees=[]

def add_employee():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    salary = float(input("Enter salary: "))

    employee ={
        "name": name,
        "emp_id": emp_id,
        "salary": salary
    }

    Employees.append(employee)
    print("Employee added successfully!")




#----------------------------------------------------------


def view_employees():
    if not Employees:
        print("No employees found.")
        return

    for emp in Employees:
        print("------------------------------------ ")
        print("Name:", emp["name"])
        print("Employee ID:", emp["emp_id"])
        print("Salary:", emp["salary"]) 
        
        
        
def update_employee():
    emp_id =input("Enter employee ID to update: ")
    for emp in Employees:
        if emp["emp_id"] ==emp_id:
            print("Current details:")
            print("Name:", emp["name"])
            print("Salary:", emp["salary"])
            
            new_name=input("enter the name to update:")
            new_salary=float(input("enter the salary to update:"))
            emp["name"]=new_name
            emp["salary"]=new_salary
            print("Employee details updated successfully!")
             
# update_employee()



while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")

        

view_employees()

