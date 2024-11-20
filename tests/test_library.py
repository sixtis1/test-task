import unittest
import os
from use_cases.library import Library
from entities.book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        # Используем тестовый файл для хранения данных
        self.test_storage = "test_library.json"
        self.library = Library(storage_file=self.test_storage)

    def tearDown(self):
        # Удаляем тестовый файл после каждого теста
        if os.path.exists(self.test_storage):
            os.remove(self.test_storage)
        # Сбрасываем счетчик ID
        Book.id_counter = 0

    def test_add_book(self):
        self.library.add_book("Test Title", "Test Author", 2020)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Title")

    def test_remove_book(self):
        self.library.add_book("Test Title", "Test Author", 2020)
        book_id = self.library.books[0].id
        result = self.library.remove_book(book_id)
        self.assertTrue(result)
        self.assertEqual(len(self.library.books), 0)

    def test_find_books(self):
        self.library.add_book("Test Title", "Test Author", 2020)
        self.library.add_book("Another Title", "Another Author", 2021)
        results = self.library.find_books(title="Test Title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Test Author")

    def test_change_status(self):
        self.library.add_book("Test Title", "Test Author", 2020)
        book_id = self.library.books[0].id
        result = self.library.change_status(book_id, "выдана")
        self.assertTrue(result)
        self.assertEqual(self.library.books[0].status, "выдана")

if __name__ == '__main__':
    unittest.main()
