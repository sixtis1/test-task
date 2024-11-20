from use_cases.library import Library
from interfaces.console_interface import ConsoleInterface

def main():
    library = Library()

    while True:
        ConsoleInterface.display_menu()

        choice = ConsoleInterface.get_user_input("Введите номер действия: ")

        match choice:

            case '1':
                title = ConsoleInterface.get_user_input("Введите название книги: ")
                author = ConsoleInterface.get_user_input("Введите автора книги: ")
                try:
                    year = int(ConsoleInterface.get_user_input("Введите год издания книги: "))
                except ValueError:
                    ConsoleInterface.display_message("Год издания должен быть числом.")
                    continue
                library.add_book(title, author, year)
                ConsoleInterface.display_message("Книга успешно добавлена.")

            case '2':
                try:
                    book_id = int(ConsoleInterface.get_user_input("Введите ID книги для удаления: "))
                except ValueError:
                    ConsoleInterface.display_message("ID должен быть числом.")
                    continue
                if library.remove_book(book_id):
                    ConsoleInterface.display_message("Книга успешно удалена.")
                else:
                    ConsoleInterface.display_message("Книга с таким ID не найдена.")
    
            case '3':
                key = ConsoleInterface.get_user_input("Введите поле для поиска (title, author, year): ")
                if key not in ["title", "author", "year"]:
                    ConsoleInterface.display_message("Некорректное поле для поиска.")
                    continue
                value = ConsoleInterface.get_user_input("Введите значение для поиска: ")
                if key == "year":
                    try:
                        value = int(value)
                    except ValueError:
                        ConsoleInterface.display_message("Год издания должен быть числом.")
                        continue
                results = library.find_books(**{key: value})
                if results:
                    for book in results:
                        ConsoleInterface.display_message(
                            f"ID: {book.id}, Название: {book.title}, "
                            f"Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
                        )
                else:
                    ConsoleInterface.display_message("Книги не найдены.")
    
            case '4':
                if library.books:
                    for book in library.books:
                        ConsoleInterface.display_message(
                            f"ID: {book.id}, Название: {book.title}, "
                            f"Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
                        )
                else:
                    ConsoleInterface.display_message("Библиотека пуста.")
    
            case '5':
                try:
                    book_id = int(ConsoleInterface.get_user_input("Введите ID книги для изменения статуса: "))
                except ValueError:
                    ConsoleInterface.display_message("ID должен быть числом.")
                    continue
                new_status = ConsoleInterface.get_user_input("Введите новый статус (в наличии/выдана): ")
                if new_status not in ["в наличии", "выдана"]:
                    ConsoleInterface.display_message("Некорректный статус.")
                    continue
                if library.change_status(book_id, new_status):
                    ConsoleInterface.display_message("Статус книги успешно обновлен.")
                else:
                    ConsoleInterface.display_message("Книга с таким ID не найдена.")
    
            case '6':
                ConsoleInterface.display_message("Спасибо за использование программы.")
                break
    
            case _:
                ConsoleInterface.display_message("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
