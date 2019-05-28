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

while True:
    user_response = input("What would you like to do? \n> "
                        "1. Add a note \n> "
                        "2. Print a note \n> "
                        "3. Exit \n> "
    )

    if user_response == "1":
        content = input("What is the note? \n> ")
        note_id = counter
        counter += 1
        note = (note_id, str(now), content)
        notebook.append(note)
    elif user_response == "2":
        for note in notebook:
            print(f"ID: {note[0]}| {note[2]}")
    elif user_response == "3":
        exit()
    else:
        print("Invalid input")


print(notebook)


