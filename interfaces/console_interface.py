class ConsoleInterface:
    """
    Класс для взаимодействия с пользователем через консоль.
    """

    @staticmethod
    def display_menu():
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

    @staticmethod
    def get_user_input(prompt: str) -> str:
        return input(prompt)

    @staticmethod
    def display_message(message: str) -> None:
        print(message)
