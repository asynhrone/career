from flask import Flask, render_template, redirect, flash, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask_cors import CORS
from functions import fetch_and_parse_news

app = Flask(__name__)
CORS(app)
mysql = MySQL(app)

CORS(app, origins=["http://localhost:5000"])
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "database"


@app.route('/')
def index():
    techno_url = 'https://new-science.ru/category/tehnologii/'
    techno_news = fetch_and_parse_news(techno_url, 5)

    maybe_interesting_url = 'https://new-science.ru/category/astronomiya/'
    maybe_interesting_news = fetch_and_parse_news(maybe_interesting_url, 7)  

    big_article = techno_news[0] if techno_news else None
    articles = techno_news[1:] if len(techno_news) > 1 else []

    return render_template('home.html',
                           big_article=big_article,
                           articles=articles,
                           maybe_interesting_news=maybe_interesting_news)


if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)