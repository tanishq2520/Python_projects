students={} #mind it:we cannot change the keys means names are immutable
def add_student(name,grade):
    students[name] = grade
    print(f"{name} added with grades {grade}")

def update_student(name,grade):
    if name in students:
        students[name] = grade
        print(f"{name} updated with grades {grade}")
    else:
        print(f"Student {name} does not exist")

def delete_student(name):
    if name in students:
        del students[name]
        print(f"{name} deleted")
    else:
        print(f"Student {name} does not exist")

def display_students():
    for name,grade in students.items():
        print("------------------")
        print(f"{name} : {grade}")

def main():
    while True:
        print("1 : Add Record")
        print("2 : Update Record")
        print("3 : Delete Record")
        print("4 : Display Record")
        print("5 : Exit Record")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter your name: ")
            grade = int(input("Enter your grade: "))
            add_student(name,grade)
        elif choice == 3:
            name = input("Enter the name of student you want to delete :")
            delete_student(name)
        elif choice == 2:
            name = input("Enter the name of student you want to update: ")
            grade = int(input("Enter your grade: "))
            update_student(name, grade)
        elif choice == 4:
            display_students()
        elif choice == 5:
            print("Record is closing")
            break
        else:
            print("Invalid choice")

main()







