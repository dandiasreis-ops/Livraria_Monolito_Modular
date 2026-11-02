"""Consultas simples de disponibilidade, isoladas no módulo de estoque."""
from modules.catalog.repository import find_book


def is_available(book_or_id):
    book = find_book(book_or_id) if isinstance(book_or_id, int) else book_or_id
    return bool(book and book.stock > 0)
