# Create an empty dictionary to store student information
students = {}

while True:
    print("\nClassroom Management System Menu:")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. Update Student Information")
    print("5. Remove a Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # Add Student
        roll_number = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        students[roll_number] = {'Name': name, 'Age': age, 'Grade': grade}
        print(f"Student with Roll Number {roll_number} added successfully.")

    elif choice == '2':
        # View All Students
        print("List of all students:")
        if not students:
            print("No students in the class.")
        else:
            for roll_number, details in students.items():
                print(f"Roll Number: {roll_number}, Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}")

    elif choice == '3':
        # Search for a Student
        search_roll_number = int(input("Enter Roll Number to search: "))
        if search_roll_number in students:
            details = students[search_roll_number]
            print(f"Details for Roll Number {search_roll_number}: Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}")
        else:
            print(f"Error: Student with Roll Number {search_roll_number} not found.")

    elif choice == '4':
        # Update Student Information
        update_roll_number = int(input("Enter Roll Number to update: "))
        if update_roll_number in students:
            students[update_roll_number]['Age'] = int(input("Enter new Age: "))
            students[update_roll_number]['Grade'] = input("Enter new Grade: ")
            print(f"Student with Roll Number {update_roll_number} updated successfully.")
        else:
            print(f"Error: Student with Roll Number {update_roll_number} not found.")

    elif choice == '5':
        # Remove a Student
        remove_roll_number = int(input("Enter Roll Number to remove: "))
        if remove_roll_number in students:
            del students[remove_roll_number]
            print(f"Student with Roll Number {remove_roll_number} removed successfully.")
        else:
            print(f"Error: Student with Roll Number {remove_roll_number} not found.")

    elif choice == '6':
        # Exit the program
        print("Exiting the Classroom Management System.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
