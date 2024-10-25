def main_menu():
    while True:
        print("\nFlashcards Learning Tool")
        print("1. Add a Flashcard")
        print("2. View Flashcards")
        print("3. Start Quiz")
        print("4. Delete a Flashcard")
        print("5. Exit")

        choice = input("Please select an option (1-6): ")

        if choice == "1":
            add_flashcard()
        elif choice == "2":
            view_flashcards()
        elif choice == "3":
            start_quiz()
        elif choice == "4":
            delete_flashcard()
        elif choice == "5":
            save_flashcards()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

