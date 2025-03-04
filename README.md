### Book Store Management System (CLI)

#### Overview
A command-line-based Book Store Management System using Python. This project ensures efficient book management with essential functionalities such as adding, viewing, searching, and removing books, along with persistent data storage.

#### Features
- **Add Books**: Users can add books with details like Title, Author, ISBN, Genre, Price, and Quantity.
- **Prevent Duplicate ISBNs**: Ensures each book has a unique ISBN.
- **View Books**: Displays all stored books in a structured format.
- **Search Books**: Allows users to search for books by title or author.
- **Remove Books**: Enables deletion of books using ISBN.
- **Data Persistence**: Uses JSON for saving and loading books automatically.
- **Error Handling**: Ensures valid user input and meaningful error messages.

#### File Structure
```
bookstore_cli/
│── main.py           # Entry point with the menu system
│── book_data.py      # Handles loading and saving book data
│── add_book.py       # Functionality for adding books
│── view_books.py     # Functionality for viewing books
│── search_books.py   # Functionality for searching books
│── remove_book.py    # Functionality for removing books
│── books.json        # Data storage file
│── design_plan.png   # Application design sketch
```

#### Usage
1. Run `main.py` to start the program.
2. Choose an option from the menu to add, view, search, or remove books.
3. Books are automatically saved to `books.json` after each change.
4. Exit the program to save and close operations.

#### Sample Menu
```
Welcome to Book Store Management System!
1. Add Book
2. View Books
3. Search Book
4. Remove Book
5. Exit
Enter your choice: 
```

#### Notes
- No external libraries are used.
- The system runs entirely on the command line.
- Modular structure ensures maintainability and reusability.
