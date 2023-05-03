from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_book import Base, BookStore, BookItem

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:root@localhost/bookstore')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# 1. JSON return 함수 구현 할 것
@app.route('/bookstores/<int:bookstore_id>/booklist/JSON')
def bookListJSON(bookstore_id):
    return ""



# 2. bookList 함수 구현 할 것 (booklist.html template 구축해야 함)
@app.route('/')
@app.route('/bookstores/<int:bookstore_id>/booklist')
def bookList(bookstore_id=None):
    return ""


# 3. newBookItem 함수 구현 할 것 (newbook.html template 구축해야 함)
@app.route('/bookstores/<int:bookstore_id>/new', methods=['GET', 'POST'])
def newBookItem(bookstore_id):

    return ""


# 4. editBookItem 함수 구현 할 것 (editbook.html template 구축해야 함)
@app.route('/bookstores/<int:bookstore_id>/<int:book_id>/edit',
           methods=['GET', 'POST'])
def editBookItem(bookstore_id, book_id):
    return ""


# 5. deleteBookItem 함수 구현 할 것 (deletebook.html template 구축해야 함)
@app.route('/bookstores/<int:bookstore_id>/<int:book_id>/delete',
           methods=['GET', 'POST'])
def deleteBookItem(bookstore_id, book_id):
    return ""


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
