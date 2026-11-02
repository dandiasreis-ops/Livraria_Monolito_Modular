"""Regras de negócio do catálogo."""
from .repository import all_books, find_book, search_books, categories


def get_catalog(query="", category=""):
    return search_books(query, category)


def get_book_details(book_id):
    return find_book(book_id)


def get_categories():
    return categories()
