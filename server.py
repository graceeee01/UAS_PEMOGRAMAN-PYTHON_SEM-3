from flask import Flask, request, jsonify

app = Flask(__name__)

# Simpan data buku di dalam list
books = [
    {"id": 1, "title": "Python for Beginners", "author": "John Doe"},
    {"id": 2, "title": "Flask Web Development", "author": "Jane Smith"}
]

# Endpoint GET untuk mengambil semua buku
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books}), 200

# Endpoint POST untuk menambahkan buku baru
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if "title" not in new_book or "author" not in new_book:
        return jsonify({"message": "Invalid data"}), 400
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return jsonify({"message": "Book added", "book": new_book}), 201

# Endpoint PUT untuk memperbarui data buku berdasarkan ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book.update(updated_data)
            return jsonify({"message": "Book updated", "book": book}), 200
    return jsonify({"message": "Book not found"}), 404

# Endpoint DELETE untuk menghapus buku berdasarkan ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
