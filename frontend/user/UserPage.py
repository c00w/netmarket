from frontend import app, db 
from frontend.page_util import has_fields
from frontend.user import logged_in
from flask.ext.login import login_required, login_user
from UserClass import User
import flask
import hashlib
import os

try:
    import simplejson as json
except ImportError:
    import json

@app.route("/login", methods=["GET", "POST"])
def login():
    if logged_in():
        return flask.redirect("/")

    if has_fields(flask.request.form, ["Username", "Password", "Method"]): 
        
        if flask.request.form["Method"] == "Login": 
            return verify_login_user(flask.request.form)
        elif flask.request.form["Method"] == "Register":
            return register_user(flask.request.form)
    
    return flask.render_template("user/login.html")

def hash_password(password, salt=None):
    if salt == None:
       salt = os.urandom(16)
    password = password.encode("utf-8") 
    return hashlib.sha512(hashlib.sha512(password + salt).hexdigest()+salt).hexdigest(), salt 

def verify_login_user(form):
    username = form['Username']
    password = form['Password']
    user = User.get_user(username) 
    if user == None:
        flask.flash("Incorrect Credentials")
        return flask.redirect("/login")
        
    if hash_password(password, user.salt)[0] == user.hashpass:
        login_user(user)
        return flask.redirect("/")
    else:
        flask.flash("Incorrect Credentials")
        return flask.redirect("/login") 

def register_user(form):
    username = form['Username']
    password = form['Password']
    user = User.get_user(username)
    if user == None:
        password, salt = hash_password(password)
        new = User(username, password, salt)
        new.save_to_db()
        login_user(new, remember=True) 
        return flask.redirect("/")
    flask.flash("Username already chosen")
    return flask.redirect("/login")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)
