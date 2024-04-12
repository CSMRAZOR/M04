# Owen Mills 4/12/2024
# M04 Lab - Case Study: Python APIs

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample book list table
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "publisher": "123 Books"},
    {"id": 2, "title": "Book 2", "author": "Author 2", "publisher": "321 Books"},
    {"id": 3, "title": "Book 3", "author": "Author 3", "publisher": "ABC Books"}
]


# Get all books
@app.route('/book', methods=['GET'])
def get_books():
    return books


# get a specific book by id
@app.route('/book/<int:book_id>', methods = ['GET'])
def get_book(book_id):
    for book in books:
        if book['id']==book_id:
            return book
        
    # If book id was not found return error    
    return {'error': 'Book not found'}


# Create a new book
@app.route('/book', methods = ['post'])
def create_book():
    new_book = {'id': len(books)+1, 'title': request.json ['title'], 'author': request.json ['author']}
    books.append(new_book)
    return new_book


# Update a books
@app.route('/book/<int:book_id>', methods = ['PUT'])
def update_book(book_id):
    for book in books:
        if book ['id'] == book_id:
            book['title'] = request.json ['title']
            book['author'] = request.json ['author']
            return book

    # If book id was not found return error    
    return {'error': 'Book not found'}


# Deleate a book
@app.route('/book/<int:book_id>', methods = ['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return{"data": "Book was deleted"}
        
    # If book id was not found return error
    return {'error': 'Book not found'}


if __name__ == '__main__':
    app.run(debug=True)
