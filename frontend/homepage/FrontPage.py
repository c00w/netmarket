import flask
from frontend import app
from frontend.user import logged_in
@app.route("/")
def frontpage():
    return flask.render_template("homepage/index.html", logged_in = logged_in())


