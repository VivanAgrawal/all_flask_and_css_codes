from flask import Flask

app = Flask(__name__)

# A dictionary to store book details by their IDs
books = {
    1: {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    2: {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    3: {'title': '1984', 'author': 'George Orwell'},
}

@app.route('/')
def home():
    return "Welcome to our bookstore!"

@app.route('/books/<int:book_id>')
def book_details(book_id):
    if book_id in books:
        book = books[book_id]
        title = book['title']
        author = book['author']
        return f"Displaying details for Book {book_id}: {title} by {author}"
    else:
        return "Book not found"