import csv
import os

FILE = "students.csv"

# Create CSV file if it does not exist
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll Number", "Name", "Marks"])


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    with open(FILE, "r", newline="") as f:
        students = list(csv.reader(f))

    for student in students[1:]:
        if student[0] == roll:
            print("Roll number already exists!")
            return

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


def search_student():
    roll = input("Enter Roll Number to search: ")

    with open(FILE, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)

        for student in reader:
            if student[0] == roll:
                print("Student Found!")
                print("Roll Number:", student[0])
                print("Name:", student[1])
                print("Marks:", student[2])
                return

    print("Student not found!")


def delete_student():
    roll = input("Enter Roll Number to delete: ")

    with open(FILE, "r", newline="") as f:
        students = list(csv.reader(f))

    updated = [students[0]]
    found = False

    for student in students[1:]:
        if student[0] == roll:
            found = True
        else:
            updated.append(student)

    if found:
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(updated)
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def display_students():
    with open(FILE, "r", newline="") as f:
        reader = csv.reader(f)
        for student in reader:
            print(student)


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
