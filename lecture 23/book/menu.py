from manager import BookManager
from ui import add_book_ui, list_books_ui, search_book_ui


def show_menu() -> None:
    """Print the main menu."""
    print("\n=== Book Management ===")
    print("1. Add a book")
    print("2. List all books")
    print("3. Search for a book")
    print("0. Exit")


def run_menu() -> None:
    """Run the menu loop until the user chooses to exit."""
    manager = BookManager()
    actions = {
        "1": add_book_ui,
        "2": list_books_ui,
        "3": search_book_ui,
    }

    while True:
        show_menu()
        choice = input("Choose: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Error: choose a number from 0 to 3!")