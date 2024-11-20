from dataclasses import dataclass, field
from typing import ClassVar, Optional

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
    id: Optional[int] = field(default=None)

    def __post_init__(self):
        if self.id is None:
            Book.id_counter += 1
            self.id = Book.id_counter
        else:
            Book.id_counter = max(Book.id_counter, self.id)
