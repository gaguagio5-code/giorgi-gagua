class Book:
    """Represents a book (encapsulation: protected attributes, read access via properties)."""

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

    def to_dict(self) -> dict:
        """Convert the book to a dictionary so it can be saved as JSON."""
        return {
            "type": "book",
            "title": self._title,
            "author": self._author,
            "year": self._year,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        """Create a book from a dictionary (the reverse of to_dict)."""
        return cls(data["title"], data["author"], data["year"])

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

    # Polymorphism: these methods are overridden
    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "ebook"
        data["file_size_mb"] = self._file_size_mb
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "EBook":
        return cls(data["title"], data["author"], data["year"], data["file_size_mb"])

    def __str__(self) -> str:
        return f"[E-Book] {super().__str__()}, {self._file_size_mb} MB"


def book_from_dict(data: dict) -> Book:
    """Pick the right class based on the saved 'type' field."""
    if data.get("type") == "ebook":
        return EBook.from_dict(data)
    return Book.from_dict(data)