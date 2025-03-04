import json
import os

db_file = "books.json"

def load_books():
    if os.path.exists(db_file):
        with open(db_file, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(db_file, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()
    isbn = input("Enter ISBN: ")
    if any(book["ISBN"] == isbn for book in books):
        print("Book with this ISBN already exists!")
        return
    title = input("Enter title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    book = {"ISBN": isbn, "Title": title, "Author": author, "Genre": genre, "Price": price, "Quantity": quantity}
    books.append(book)
    save_books(books)
    print("Book added successfully!")

def view_books():
    books = load_books()
    if not books:
        print("No books available.")
        return
    for book in books:
        print(f"ISBN: {book['ISBN']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Price: ${book['Price']}, Quantity: {book['Quantity']}")

def search_book():
    books = load_books()
    term = input("Enter title or author to search: ").lower()
    results = [book for book in books if term in book['Title'].lower() or term in book['Author'].lower()]
    if results:
        for book in results:
            print(f"ISBN: {book['ISBN']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Price: ${book['Price']}, Quantity: {book['Quantity']}")
    else:
        print("No matching books found.")

def remove_book():
    books = load_books()
    isbn = input("Enter ISBN of the book to remove: ")
    books = [book for book in books if book["ISBN"] != isbn]
    save_books(books)
    print("Book removed successfully!")

def main():
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
