# Library Management System

This console application is designed for managing a library of books. The application allows you to add, remove, search, and display books, as well as change their status.

## Features

- **Add a Book**: Enter the title, author, and year of publication.
- **Remove a Book**: Remove a book by its unique identifier.
- **Search for a Book**: Search by title, author, or year of publication.
- **Display All Books**: Display a list of all books with detailed information.
- **Change Book Status**: Update the status of a book to "available" or "checked out".
- **Data Storage**: Data is stored in JSON format.
- **Error Handling**: Proper handling of exceptions and errors.
- **Object-Oriented Approach**: Code is organized according to SOLID principles and Clean Architecture.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sixtis1/test-task.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd test-task
    ```

3. **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

## Running the Application

```bash
python main.py
```


## Project Structure
```bash
library-management-system/
├── entities/
│   └── book.py
├── use_cases/
│   └── library.py
├── interfaces/
│   └── console_interface.py
├── tests/
│   └── test_library.py
├── library.json
├── main.py
└── README.md
```

* **entities**: Contains domain entities (the Book class).
* **use_cases**: Contains the business logic of the application (the Library class).
* **interfaces**: Contains interfaces for user interaction.
* **tests**: Contains unit tests for the application.
* **library.json**: File for storing book data.
* **main.py**: Entry point of the application.

## Testing

To run the tests, execute:
```bash
python -m unittest discover -s tests
```