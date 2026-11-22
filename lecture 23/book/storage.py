import json
from pathlib import Path

from book import Book, book_from_dict

# books.json is stored next to this file
DEFAULT_PATH = Path(__file__).with_name("books.json")


def save_books(books: list[Book], path: Path = DEFAULT_PATH) -> None:
    """Write all books to a JSON file."""
    data = [book.to_dict() for book in books]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_books(path: Path = DEFAULT_PATH) -> list[Book]:
    """Read books from a JSON file. Returns an empty list if there is no usable file."""
    path = Path(path)
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [book_from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError, TypeError):
        print(f"Warning: could not read {path.name}. Starting with an empty list.")
        return []