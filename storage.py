import json
import os
from models import Book

STORAGE_FILE = "books.json"

def load_books():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book.from_dict(book) for book in data]
    return []

def save_books(books):
    data = [book.to_dict() for book in books]
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

":)"
def add_book(books, new_book):
    # Проверка на дубликаты
    for book in books:
        if book.author == new_book.author and book.title == new_book.title:
            return False
    books.append(new_book)
    save_books(books)
    return True

def delete_book(books, title, author):
    for i, book in enumerate(books):
        if book.title == title and book.author == author:
            del books[i]
            save_books(books)
            return True
    return False
