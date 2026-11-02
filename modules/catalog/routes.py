"""Rotas web do módulo de catálogo."""
from flask import Blueprint, render_template, request, abort
from .services import get_catalog, get_book_details, get_categories, get_catalog

from modules.inventory.services import is_available


catalog_bp = Blueprint("catalog", __name__)


@catalog_bp.get("/")
def index():
    query = request.args.get("q", "")
    category = request.args.get("category", "")
    books = get_catalog(query, category)
    return render_template("index.html", books=books, query=query,
                         selected_category=category, categories=get_categories(),
                         total=len(get_catalog()), is_available=is_available)


@catalog_bp.get("/livro/<int:book_id>")
def details(book_id):
    book = get_book_details(book_id)
    if book is None:
        abort(404)
    return render_template("details.html", book=book, is_available=is_available)


@catalog_bp.get("/health")
def health():
    return {"status": "ok", "module": "catalog"}
