from book import Book
from manager import BookManager
from validation import input_non_empty, input_year


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