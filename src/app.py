from flask import Flask, request
from flask import Flask, jsonify, request, render_template
from src.users import Users
from models import database

app = Flask(__name__)


@app.route("/")
def front_page():
    return render_template("frontpage.html")


@app.before_first_request
def initialize_db():
    database.create_table()


@app.route("/frontpage/login", methods=['POST', 'GET'])
def second_page():
    if request.method == 'POST':
            fname = request.form['fname']
            lname = request.form['lname']
            username = request.form['username']
            password = request.form['password']
            Users.sign(fname, lname, username, password)
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/frontpage/page1", methods=['POST'])
def home_page():
    user_name = request.form['user_name']
    password = request.form['password']

    if Users.login(user_name, password):
        user = user_name
    else:
        user = None

    return render_template("home.html")


app.run(port=4001)
