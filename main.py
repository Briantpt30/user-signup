from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html", title="Signup")

@app.route("/welcome",)
def welcome():
    name = request.args.get('name')
    return render_template('welcome.html', name=name, title="Welcome")

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
    if verify == pw:
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
    spider_man = True

    if valid_text_length(username) == False or no_spaces(username) == False:
        username_error = "That's not a valid username"
        spider_man = False
    if valid_text_length(password) == False or no_spaces(password) == False:
        pw_error= "That's not a valid password"
        spider_man = False
    if verify_pw(password, verify_pass) == False:
        verify_error="Passwords dont't match"
        spider_man = False
    if not email == '':
        if verify_email(email) == False:
            email_error = "That's not a valid email"
            spider_man = False


    if spider_man == True:
        name = username
        return redirect("/welcome?name={0}".format(name))    
    else:
        return render_template('index.html', username=username,
        username_error=username_error,
        pw_error=pw_error,
        verify_error=verify_error,
        email_error=email_error,email=email)









app.run()    