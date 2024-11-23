import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('books.db')

# Create a cursor object
cursor = conn.cursor()

# Create the books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
''')

# Function to insert a book
def insert_book(title, author):
    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()
    print(f"Inserted book: {title} by {author}")

# Function to retrieve books by a specific author
def retrieve_books_by_author(author):
    cursor.execute('SELECT * FROM books WHERE author = ?', (author,))
    rows = cursor.fetchall()
    if rows:
        print(f"Books by {author}:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}")
    else:
        print(f"No books found by {author}.")

# Insert some example books
insert_book('The Catcher in the Rye', 'J.D. Salinger')
insert_book('To Kill a Mockingbird', 'Harper Lee')
insert_book('1984', 'George Orwell')
insert_book('Animal Farm', 'George Orwell')

# Retrieve books by a specific author
author_name = 'George Orwell'
retrieve_books_by_author(author_name)

# Close the connection
conn.close()
