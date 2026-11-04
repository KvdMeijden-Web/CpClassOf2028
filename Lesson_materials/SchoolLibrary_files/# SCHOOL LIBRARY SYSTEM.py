import json
from pathlib import Path

FILE = Path(__file__).with_name("books.json")


def load_books():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_books():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)


def show_books():
    print("\n--- LIBRARY BOOKS ---")
    for book_id, book in books.items():
        status = "Available" if book["borrowed_by"] is None else "Borrowed by " + book["borrowed_by"]
        print(book_id, "-", book["title"], "-", status)


def add_book():
    title = input("Book title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    book_id = str(max((int(i) for i in books), default=0) + 1)
    books[book_id] = {"title": title, "borrowed_by": None}
    save_books()
    print("Book added!")


def borrow_book():
    show_books()
    book_id = input("Book ID: ").strip()
    if book_id not in books:
        print("Book does not exist.")
    elif books[book_id]["borrowed_by"] is not None:
        print("Book is already borrowed.")
    else:
        name = input("Student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        books[book_id]["borrowed_by"] = name
        save_books()
        print("Book borrowed!")


def return_book():
    book_id = input("Book ID to return: ").strip()
    if book_id not in books:
        print("Book does not exist.")
    elif books[book_id]["borrowed_by"] is None:
        print("Book was not borrowed.")
    else:
        books[book_id]["borrowed_by"] = None
        save_books()
        print("Book returned!")


def search_book():
    query = input("Search title: ").strip().lower()
    found = False
    for book_id, book in books.items():
        if query in book["title"].lower():
            print(book_id, "-", book["title"])
            found = True
    if not found:
        print("No books found.")


def main():
    actions = {"1": show_books, "2": add_book, "3": borrow_book,
               "4": return_book, "5": search_book}
    while True:
        print("\n===== SCHOOL LIBRARY =====")
        print("1. Show all books\n2. Add a book\n3. Borrow a book")
        print("4. Return a book\n5. Search for a book\n6. Exit")
        choice = input("Choose 1-6: ").strip()
        if choice == "6":
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid option.")


books = load_books()
main()