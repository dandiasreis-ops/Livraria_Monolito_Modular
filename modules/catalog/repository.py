from .models import Book

# Dados demonstrativos em memória; não representam estoque real.
_BOOKS = [
    Book(1, "O Hobbit", "J. R. R. Tolkien", "Fantasia", 49.90, 8,
         "Bilbo Bolseiro parte em uma aventura inesperada com um grupo de anões.", "HarperCollins", 1937),
    Book(2, "1984", "George Orwell", "Ficção distópica", 39.90, 0,
         "Um clássico sobre vigilância, poder e liberdade em uma sociedade totalitária.", "Companhia das Letras", 1949),
    Book(3, "Dom Casmurro", "Machado de Assis", "Literatura brasileira", 29.90, 5,
         "Romance narrado por Bento Santiago, que revisita lembranças de sua vida.", "Principis", 1899),
    Book(4, "A Sociedade do Anel", "J. R. R. Tolkien", "Fantasia", 59.90, 3,
         "A primeira parte da jornada para destruir o Um Anel.", "HarperCollins", 1954),
    Book(5, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Fábula", 24.90, 12,
         "Uma narrativa poética sobre amizade, afeto e o modo como vemos o mundo.", "Agir", 1943),
    Book(6, "Capitães da Areia", "Jorge Amado", "Literatura brasileira", 34.90, 2,
         "A história de um grupo de meninos que vive nas ruas de Salvador.", "Companhia das Letras", 1937),
]

def all_books():
    return list(_BOOKS)

def find_book(book_id):
    return next((b for b in _BOOKS if b.id == book_id), None)

def search_books(query="", category=""):
    query, category = query.strip().casefold(), category.strip().casefold()
    result = _BOOKS
    if query:
        result = [b for b in result if query in b.title.casefold() or query in b.author.casefold()]
    if category:
        result = [b for b in result if b.category.casefold() == category]
    return list(result)

def categories():
    return sorted({b.category for b in _BOOKS})
