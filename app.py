from flask import Flask, render_template, redirect, flash, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
mysql = MySQL(app)

CORS(app, origins=["http://localhost:5000"])
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "database"

@app.route('/')
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)