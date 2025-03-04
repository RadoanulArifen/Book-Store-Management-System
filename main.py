import json
import os

# File to store book data
db_file = "book.txt"

def load_books():
    """Load books from the book.txt file."""
    if os.path.exists(db_file):
        with open(db_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Return empty list if file is empty or corrupted
    return []

def save_books(books):
    """Save book list to book.txt file."""
    with open(db_file, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    """Add a new book to the store."""
    books = load_books()
    isbn = input("Enter ISBN: ").strip()

    # Check for duplicate ISBN
    if any(book["ISBN"] == isbn for book in books):
        print("❌ Book with this ISBN already exists!")
        return

    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    genre = input("Enter genre: ").strip()

    # Validate price and quantity
    try:
        price = float(input("Enter price: "))
        if price <= 0:
            raise ValueError("Price must be a positive number.")
    except ValueError as e:
        print(f"❌ Invalid price: {e}")
        return

    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
    except ValueError as e:
        print(f"❌ Invalid quantity: {e}")
        return

    # Create book dictionary
    book = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "Genre": genre,
        "Price": price,
        "Quantity": quantity
    }

    books.append(book)
    save_books(books)
    print("✅ Book added successfully!")

def view_books():
    """View all books in the store."""
    books = load_books()
    if not books:
        print("📚 No books available.")
        return

    print("\n📖 Book List:")
    print("=" * 50)
    for book in books:
        print(f"ISBN: {book['ISBN']}")
        print(f"Title: {book['Title']}")
        print(f"Author: {book['Author']}")
        print(f"Genre: {book['Genre']}")
        print(f"Price: ${book['Price']:.2f}")
        print(f"Quantity: {book['Quantity']}")
        print("-" * 50)

def search_book():
    """Search for a book by title or author."""
    books = load_books()
    term = input("Enter title or author to search: ").strip().lower()

    results = [book for book in books if term in book['Title'].lower() or term in book['Author'].lower()]
    if results:
        print("\n🔍 Search Results:")
        print("=" * 50)
        for book in results:
            print(f"ISBN: {book['ISBN']}")
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Genre: {book['Genre']}")
            print(f"Price: ${book['Price']:.2f}")
            print(f"Quantity: {book['Quantity']}")
            print("-" * 50)
    else:
        print("❌ No matching books found.")

def remove_book():
    """Remove a book by ISBN."""
    books = load_books()
    isbn = input("Enter ISBN of the book to remove: ").strip()

    if not any(book["ISBN"] == isbn for book in books):
        print("❌ No book found with this ISBN.")
        return

    books = [book for book in books if book["ISBN"] != isbn]
    save_books(books)
    print("✅ Book removed successfully!")

def main():
    """Main menu for the Book Store Management System."""
    while True:
        print("\n📚 Book Store Management System")
        print("1️⃣ Add Book")
        print("2️⃣ View Books")
        print("3️⃣ Search Book")
        print("4️⃣ Remove Book")
        print("5️⃣ Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("👋 Exiting program... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
