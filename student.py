import os

students = []

def clear_consol():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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
    print(input("press Enter to continue.."))
        
#def list_students():  

#def search_student():

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