FILE_NAME = "notes.txt"

def notes_menu():
    while True:
        print("\n--- NOTES APP ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            note = input("Enter your note: ")
            with open(FILE_NAME, "a") as file:
                file.write(note + "\n")
            print("Note saved ✅")

        elif choice == "2":
            try:
                with open(FILE_NAME, "r") as file:
                    notes = file.read()
                    if notes.strip():
                        print("\nYour Notes:")
                        print(notes)
                    else:
                        print("No notes found.")
            except FileNotFoundError:
                print("No notes file yet.")

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")

