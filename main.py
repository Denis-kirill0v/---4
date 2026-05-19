from storage import load_books, save_books, add_book, delete_book
from stats import average_rating, author_stats
from models import Book

def show_menu():
    print("\n=== Трекер прочитанных книг ===")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")

def main():
    books = load_books()

    while True:
        show_menu()
        choice = input("Выберите пункт: ")

        if choice == "1":
            author = input("Автор: ")
            title = input("Название: ")
            rating = int(input("Оценка (1-5): "))
            new_book = Book(author, title, rating)
            if add_book(books, new_book):
                print("Книга добавлена!")
            else:
                print("Книга уже существует!")

        elif choice == "2":
            for book in books:
                print(f"{book.title} - {book.author} ({book.rating}/5)")

        elif choice == "3":
            avg = average_rating(books)
            print(f"Средняя оценка: {avg}")

        elif choice == "4":
            stats = author_stats(books)
            for author, count in stats.items():
                print(f"{author}: {count} книг")

        elif choice == "5":
            title = input("Название книги: ")
            author = input("Автор: ")
            if delete_book(books, title, author):
                print("Книга удалена!")
            else:
                print("Книга не найдена!")

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
