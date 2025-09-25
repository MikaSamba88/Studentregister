import os

students = []

def clear_consol():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_menu():
    print("\n1. Add Student") 
    print("2. List of Students") 
    print("3. Search Student")
    print("4. Avarage Age") 
    print("5. Exit program\n") 

def add_student():
def list_students():   
def search_student():
def avrage_age():
def exit_program():    

print("------------------------------------")
print("------- Register a Student  --------")
print("------------------------------------\n")

while True:
    
    choice = input("Choose a number: ")

    if choice == "1":
        name = input("Name: ")
        try:
            age = int(input("Age: "))
        except:
            print("Age must be a number! ")
            input("Press Enter..")
    
    elif choice == "2":
        if students:
            print("All Students: ")