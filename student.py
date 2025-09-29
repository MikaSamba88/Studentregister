import os
import sys
import json
import prettytable



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")

def clear_consol():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def load_student_from_file():
    global students
    try:
        with open(FILE_PATH, "r") as file:
           students = json.load(file)
    except FileNotFoundError:
        students = []
                
def save_student_to_file():
    with open (FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)

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

def add_student(student_list):
    name = input("\nName: ")

    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Age must be a number! Try again! ")
    
    email = input("Email: ")
    favorit = input("Enter your Favorit movie: ")
           
    students.append({"name": name, "age": age, "email": email, "Favorit_movie": favorit})

    print(f"\n{name} was added to the list!")
    
    save_student_to_file()

    print(input("press Enter to continue.."))
    return students
        
def list_students():
    if not students:
        print("No students added yet!")
    else:
        print("\nStudent List:")
        print("-" * 25)
        for i, s in enumerate(students, start=1):
            print(f"{i}. {s['name']} (Age: {s['age']}, Email: {s['email']}, Favorite movie: {s['Favorit_movie']})")
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


def average_age():
    if not students:
        print("\nNo students available to calculate average age...")
        print(input("Press Enter to continue.. "))
        return
    total_age = sum(s["age"] for s in students)
    average = total_age / len(students)
    print(f"\nAverage age: {average:.1f}")
    input("\nPress Enter to continue..")



def exit_program():
    clear_consol()
    print("You choose to exit!\n")
    print(input("Tryck Enter för att avsluta..."))   



def main():
    students = []
    while True:
        print_menu()
        choice = input("Choose a number: ")

        if choice == "1":
           students = add_student(students)
        
        elif choice == "2":
            list_students()

        elif choice == "3":
            search_student()
        
        elif choice == "4":
            average_age()
        
        elif choice == "5":
            exit_program()
            sys.exit()

if __name__ == "__main__":
    main()