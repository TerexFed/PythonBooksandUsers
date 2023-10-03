import json
import csv


class Book:
    title: str
    author: str
    genre: str
    pages: int
    publisher: str


with open('books.csv', 'r') as Books:
    books = []
    reader = csv.DictReader(Books, fieldnames=['title', 'author', 'genre', 'pages', 'publisher'])

    header = next(reader)

    for row in reader:
        currentBook = Book()
        currentBook.title = row['title']
        currentBook.author = row['author']
        currentBook.genre = row['genre']
        currentBook.pages = row['pages']
        currentBook.publisher = row['publisher']
        books.append(row)
with open('users.json', "r") as Users:
    users = json.loads(Users.read())

    users_len = len(users)

    books_len = len(books)

    difference = books_len // users_len

    smallUsers = []


    def give_book(smallUser, index):

        smallUser['books'] = []
        for bookNumber in range(index, index + difference):
            smallUser['books'].append(books[bookNumber])


    index = 0
    for user in users:
        smallUser = dict()

        smallUser['name'] = user['name']
        smallUser['gender'] = user['gender']
        smallUser['address'] = user['address']
        smallUser['age'] = user['age']
        give_book(smallUser, index)
        index += difference
        smallUsers.append(smallUser)
    for bookNumber in range(index, books_len):
        smallUsers[len(smallUsers)-1]['books'].append(books[bookNumber])

with open("result.json", "w") as f:
    s = json.dumps(smallUsers, indent=1)
    f.write(s)
