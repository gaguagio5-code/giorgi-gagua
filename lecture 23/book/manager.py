from pathlib import Path

from book import Book
from storage import DEFAULT_PATH, load_books, save_books


class BookManager:
    """Manages the list of books and keeps it saved in a JSON file."""

    def __init__(self, path: Path = DEFAULT_PATH):
        self._path = path
        self._books: list[Book] = load_books(self._path)

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        save_books(self._books, self._path)  # save after every change

    def list_books(self) -> list[Book]:
        # Return a copy so the internal list stays protected
        return list(self._books)

    def find_by_title(self, title: str) -> list[Book]:
        # Case-insensitive partial match; may return several books
        query = title.strip().lower()
        return [b for b in self._books if query in b.title.lower()]