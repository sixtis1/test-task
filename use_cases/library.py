import json
from typing import List
from entities.book import Book

class Library:
    """
    Класс, представляющий библиотеку и содержащий бизнес-логику.
    """

    def __init__(self, storage_file: str = "library.json"):
        self.storage_file = storage_file
        self.books: List[Book] = []
        self.load_books()

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title=title, author=author, year=year)
        self.books.append(book)
        self.save_books()

    def remove_book(self, book_id: int) -> bool:
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return True
        return False

    def find_books(self, **kwargs) -> List[Book]:
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key) == value]
        return results

    def change_status(self, book_id: int, new_status: str) -> bool:
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                return True
        return False

    def load_books(self) -> None:
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                books_data = json.load(f)
                for book_data in books_data:
                    book = Book(**book_data)
                    self.books.append(book)
        except FileNotFoundError:
            pass

    def save_books(self) -> None:
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([book.__dict__ for book in self.books], f, ensure_ascii=False, indent=4)
