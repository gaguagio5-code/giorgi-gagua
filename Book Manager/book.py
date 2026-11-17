from datetime import date

class Book:

    def __init__(self, title: str, author: str, year: int):
        self._title = title
        self._author = author
        self._year = year

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> int:
        return self._year

    def __str__(self) -> str:
        return f"{self._title} by {self._author} ({self._year})"

class EBook(Book):
    """Represents an electronic book (inheritance)."""

    def __init__(self, title: str, author: str, year: int, file_size_mb: float):
        super().__init__(title, author, year)
        self._file_size_mb = file_size_mb

    @property
    def file_size_mb(self) -> float:
        return self._file_size_mb

    def __str__(self) -> str:
        return f"[E-Book] {super().__str__()}, {self._file_size_mb} MB"

class BookManager:
    """Manages the list of books."""

    def __init__(self):
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def list_books(self) -> list[Book]:
        return list(self._books)

    def find_by_title(self, title: str) -> list[Book]:
        query = title.strip().lower()
        return [b for b in self._books if query in b.title.lower()]

def input_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: this field cannot be empty!")


def input_year(prompt: str) -> int:
    current_year = date.today().year
    while True:
        raw = input(prompt).strip()
        try:
            year = int(raw)
        except ValueError:
            print("Error: year must be a number!")
            continue
        if not 1000 <= year <= current_year:
            print(f"Error: year must be between 1000 and {current_year}!")
            continue
        return year

def add_book_ui(manager: BookManager) -> None:
    title = input_non_empty("Title: ")
    author = input_non_empty("Author: ")
    year = input_year("Year: ")
    manager.add_book(Book(title, author, year))
    print("✔ Book added.")


def list_books_ui(manager: BookManager) -> None:
    books = manager.list_books()
    if not books:
        print("The list is empty.")
        return
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book}")


def search_book_ui(manager: BookManager) -> None:
    title = input_non_empty("Title: ")
    results = manager.find_by_title(title)
    if not results:
        print("Book not found.")
        return
    for book in results:
        print(f"Found: {book}")


def main() -> None:
    manager = BookManager()
    actions = {
        "1": add_book_ui,
        "2": list_books_ui,
        "3": search_book_ui,
    }

    while True:
        print("\n=== Book Management ===")
        print("1. Add a book")
        print("2. List all books")
        print("3. Search for a book")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Error: choose a number from 0 to 3!")

if __name__ == "__main__":
    main()
