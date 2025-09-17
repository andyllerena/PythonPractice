from flask import Flask 
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify ({
        "message" : "Welcome to your own libary"
    })


library = [{"id": 1, "title": "1984", "author": "George Orwell"}]

@app.route("/library")
def view_books():

    return jsonify({
        "Library" : library
    })

@app.route("/library/<int:book_id>")
def view_book_id(book_id):

    book = None 
    for item in library:
        if item["id"] == book_id:
            title = item["title"]
            author = item["author"]
        
            book = f"Title: {title} Author: {author}"
            break

    return jsonify({
        "Book" : book
    })

    


@app.route("/library/add_book",methods=["POST"])
def add_book():
    data = request.get_json()

    if len(library) > 0:
        new_id = library[-1]["id"] + 1
    else:
        new_id = 1

    new_book = {
        "id" : new_id, "title" : data["title"], "author": data["author"]
    }

    library.append(new_book)

    return jsonify({
        "New Book Added" : new_book
    })

@app.route("/library/search/<title>", methods=["GET"])
def search_book(title):
    url = "https://openlibrary.org/search.json"
    params = {
        "q": title,
        "limit": 5
    }

    response = requests.get(url, params=params)
    data = response.json()
    books = data.get("docs", [])

    results = []
    for book in books:
        book_title = book.get("title", "No title")
        authors = book.get("author_name", ["Unknown author"])
        year = book.get("first_publish_year", "Unknown year")

        results.append({
            "title": book_title,
            "authors": authors,
            "year": year
        })

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)