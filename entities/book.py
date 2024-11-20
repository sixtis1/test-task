from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Book:
    """
    Класс, представляющий книгу в библиотеке.
    """
    id_counter: ClassVar[int] = 0
    title: str
    author: str
    year: int
    status: str = "в наличии"
    id: int = field(init=False)

    def __post_init__(self):
        Book.id_counter += 1
        self.id = Book.id_counter
