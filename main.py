from datetime import date

"""
Note Book app

Notes will have three parts:
ID
Content
Date/Time

"""
notebook = []
counter = 1
now = date.today()

def menu():
    user_response = input("What would you like to do? \n> "
                    "1. Add a note \n> "
                    "2. Print a note \n> "
                    "3. Exit \n> ")
    return user_response

def note_create():
    content = input("What is the note? \n> ")
    global counter
    note_id = counter
    counter += 1
    note = (note_id, str(now), content)
    notebook.append(note)

def print_notes():
    for note in notebook:
        print(f"ID: {note[0]}| {note[2]}")   

def run():
    while True:
        choice = menu()
        if choice == "1":
            note_create()
        elif choice == "2":
            print_notes()
        elif choice == "3":
            exit()
        else:
            print("Invalid input") 
 
if __name__ == "__main__":
     run()



