# Initialize an empty list to store student names
student_names = []

while True:
    # Display the menu options
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Students")
    print("4. Exit")
    
    # Get user choice
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Add a student
        name = input("Enter the student's name to add: ")
        student_names.append(name)
        print(f"{name} has been added.")

    elif choice == '2':
        # Remove a student
        name = input("Enter the student's name to remove: ")
        if name in student_names:
            student_names.remove(name)
            print(f"{name} has been removed.")
        else:
            print(f"{name} is not in the list.")

    elif choice == '3':
        # Display the list of students
        if student_names:
            print("List of Students:")
            for student in student_names:
                print(f"- {student}")
        else:
            print("No students in the list.")

    elif choice == '4':
        # Exit the program
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
