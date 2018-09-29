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

def verify_pw(pw, verify):
    if pw == verify:
        return True
    else:
        return False    

def verify_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False    

@app.route('/', methods=['POST'])
def validate_info():

    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify']
    email = request.form['email']

    username_error = ''
    pw_error = ''
    verify_error = ''
    email_error = ''

    if valid_text_length(username) == False and no_spaces(username) == False:
        username_error = "That's not a valid username"
    if valid_text_length(password) == False and no_spaces(password) == False:
        pw_error= "That's not a valid password"
        password=''
    if verify_pw(password, verify_pass) == False:
        verify_error="Passwords dont't match"
        verify_pass=''
    if verify_email(email) == False:
        email_error = "That's not a valid email"
        











app.run()    