from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', name=username)

def valid_text_length(text):
    if len(text) > 3 and len(text) < 20:
        return True
    else:
        return False  

def no_spaces(text):
    if ' ' in text:
        return False
    else:
        return True



app.run()    