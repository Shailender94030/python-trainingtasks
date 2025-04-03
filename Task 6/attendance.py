
employees = {}

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    employees[emp_id] = {"name": name, "age": age, "attendance": []}
    print(f"Employee {name} added successfully!\n")
def mark_attendance():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        status = input("Enter Attendance (1 for Present, 0 for Absent): ")
        if status in ["0", "1"]:
            employees[emp_id]["attendance"].append(int(status))
            print("Attendance marked successfully!\n")
        else:
            print("Invalid input. Enter 1 for Present or 0 for Absent.\n")
    else:
        print("Employee not found!\n")
def view_employees():
    for emp_id, details in employees.items():
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Attendance: {details['attendance']}")
    print()
def check_absentees():
    print("Employees with 3+ consecutive absences:")
    for emp_id, details in employees.items():
        attendance = "".join(map(str, details["attendance"]))
        if "000" in attendance:
            print(f"{details['name']} (ID: {emp_id}) Needs Attention!")
while True:
    print("\n1. Add Employee\n2. Mark Attendance\n3. View Employees\n4. Show Absentee Report\n5. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_employees()
    elif choice == "4":
        check_absentees()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")
