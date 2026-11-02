from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str
    category: str
    price: float
    stock: int
    description: str
    publisher: str
    year: int

    @property
    def available(self):
        return self.stock > 0
