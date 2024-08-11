student = {}
while True:
    print("\n Classroom Management System-2024")
    print("1-> Add student")
    print("2-> View All students")
    print("3-> Search for a student")
    print("4-> Update Student Information in Database")
    print("5-> Remove a student")
    print("6-> Exit")
    c = input("Enter your choice from (1 to 6): ")

    # Add student to the database
    if c == "1":
        roll = int(input("\nEnter the roll number: "))
        name = str(input("Enter the student name: "))
        age = int(input("Enter the student age: "))
        grade = float(input("Enter the student grade: "))
        student[roll] = {
            "Name": name,
            "Age": age,
            "Grade": grade,
        }
        print(f"Student with roll number {roll} added successfully.")

    # View all students in the database
    elif c == "2":
        print("List of all students:")
        if not student:
            print("No students in the class-2024 database.")
        else:
            for roll, d in student.items():
                print(
                    f"\nRoll number: {roll}",
                    f"\nName: {d['Name']}",
                    f"\nAge: {d['Age']}",
                    f"\nGrade: {d['Grade']}"
                )

    elif c=="3":
        search_roll=(int)(input("Enter the roll number for search in database :"))
        #searching from database :
        if search_roll in student:
            d= student[search_roll]
            print(f"Details for Roll number{search_roll}:\nName:{d['Name']},\nAge:{d['Age']},\nGrade:{d["Grade"]}")
        else:
            print(f"  Student with Roll Number {search_roll}  is not found.")
    
    elif c== '4':
        #Update database system 
        update_roll_number=(int)(input("Enter the roll number want to update :"))
        if update_roll_number in student:
            student[update_roll_number]['Age']=(int)(input("Enter the new age "))
            student[update_roll_number]['Grade']=(float)(input("Enter the updated grade:"))
            student[update_roll_number]['Name']=(str)(input("Enter the updated name :"))
            print(f"Students information with roll number {update_roll_number} updated successfully")
        else:
            print(f"Student roll number {update_roll_number} is not found in database ")    
    elif c=='5':
        #deleting from database 
        remove_roll_number=(int)(input("Enter the roll number want to remove "))
        if remove_roll_number in student:
            del student[remove_roll_number]
            print(f"Student roll number {remove_roll_number} is deleted from database successfully")
        else:
            print(f"student roll number {remove_roll_number} is not found in database ")
    elif c=='6':
        print(f"Exiting the classroom-2024 database system ")
        break;
    else:
         print(f"Invalid choice -please choose the required option")