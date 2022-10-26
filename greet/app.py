from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return f"<h2>welcome</h2>"



@app.route('/welcome/home')
def welcome_home():
    return f"<h2>Welcome home</h2>"



@app.route('/welcome/back')
def welcome_back():
    return f"<h2>Welcome back</h2>"

