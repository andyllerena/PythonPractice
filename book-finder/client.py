import requests

BASE_URL = "http://127.0.0.1:5000"

def show_menu():
    print("\n==== Library Client ====")
    print("1. View all books in your library")
    print("2. View a book by ID")
    print("3. Add a new book to your library")
    print("4. Search books online (Open Library)")
    print("q. Quit")
    print("========================")

def view_all_books():
    res = requests.get(BASE_URL + "/library")
    data = res.json()
    for book in data["Library"]:
        print(f"{book['id']}. {book['title']} by {book['author']}")

def view_book_by_id():
    book_id = input("Enter book ID: ")
    res = requests.get(BASE_URL + f"/library/{book_id}")
    data = res.json()
    print(data["Book"])

def add_new_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    new_book = {"title": title, "author": author}
    res = requests.post(BASE_URL + "/library/add_book", json=new_book)
    print(res.json())

def search_books():
    title = input("Enter a title to search: ")
    res = requests.get(BASE_URL + f"/library/search/{title}")
    results = res.json()

    print("\nSearch Results:")
    for i, book in enumerate(results, start=1):
        authors = ", ".join(book["authors"])
        print(f"{i}. {book['title']} by {authors} ({book['year']})")

def main():
    answer = ""
    while answer != "q":
        show_menu()
        answer = input("Choose an option: ").lower()

        if answer == "1":
            view_all_books()
        elif answer == "2":
            view_book_by_id()
        elif answer == "3":
            add_new_book()
        elif answer == "4":
            search_books()
        elif answer == "q":
            print("Goodbye!")
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
