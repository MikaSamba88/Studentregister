import os


students = []


def clear_consol():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def load_student_from_file():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, age = line.strip().split(",")
                students.append({"name": name, "age": int(age)})
    except FileNotFoundError:
        pass
                
def save_student_to_file():
    with open ("students.txt", "w") as file:
        for s in students:
            file.write(f"{s['name']},{s['age']}\n")

load_student_from_file()

def print_menu():
    clear_consol()
    print("------------------------------------")
    print("------- Register a Student  --------")
    print("------------------------------------\n")
    print("\n1. Add Student") 
    print("2. List of Students") 
    print("3. Search Student")
    print("4. Avarage Age") 
    print("5. Exit program\n") 

def add_student():
    name = input("\nName: ")

    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Age must be a number! Try again! ")
           
    students.append({"name": name, "age": age})
    print(f"{name} was added to the list!")
    
    save_student_to_file()

    print(input("press Enter to continue.."))
        
def list_students():
    if not students:
        print("No students added yet!")
    else:
        print("\nStudent List:")
        print("-" * 25)
        for i, s in enumerate(students, start=1):
            print(f"{i}. {s['name']} (Age: {s['age']})")
            print("-" * 25)
    print(input("\nPress Enter to continue.."))


def search_student():
    search = input("\nEnter students name to search: ")
    found = False

    for s in students:
        if s["name"].lower() == search.lower():
            print(f" Found: {s['name']} (Age: {s['age']})")
            found = True

    if not found:
        print(f"Sorry, didnt find {search}.. ")

    input("\nPress Enter to continue")


#def avrage_age():


def exit_program():
    clear_consol()
    print("You choose to exit!\n")
    print(input("Tryck Enter för att avsluta..."))   



while True:
    print_menu()
    choice = input("Choose a number: ")

    if choice == "1":
        add_student()
    
    elif choice == "2":
        list_students()

    elif choice == "3":
        search_student()
    
    elif choice == "4":
        avrage_age()
    
    elif choice == "5":
        exit_program()