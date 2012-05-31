from frontend import app
from flask.ext.login import login_required
import flask

@app.route("/login", methods=["GET", "POST"])
def login():
    if validate_login_post(flask.request.form): 
        # login and validate the user...
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("/"))
    
    return flask.render_template("user/login.html")

def validate_login_post(header):
    print header

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)
