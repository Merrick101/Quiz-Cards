def main_menu():
    while True:
        print("\nFlashcards Learning Tool")
        print("1. Add a Flashcard")
        print("2. View Flashcards")
        print("3. Start Quiz")
        print("4. Delete a Flashcard")
        print("5. Exit")

        choice = input("Please select an option (1-5): ")

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

def display_welcome_message():
    print("*****************************************")
    print("        Welcome to QuizCards!")
    print("*****************************************")
    print()
    print("The ultimate flashcard quiz tool to boost your knowledge!")
    print()
    print("With QuizCards, you can:")
    print("1. Add your own flashcards for personalized learning.")
    print("2. View all flashcards to review and reinforce your knowledge.")
    print("3. Test yourself with our Quiz mode to see how much you’ve learned.")
    print("4. Delete flashcards you no longer need to keep your study deck fresh.")
    print()
    print("Let’s get started and make learning fun and interactive!")

def main():
    """
    Run program functions
    """
    display_welcome_message()
    main_menu()

main()

