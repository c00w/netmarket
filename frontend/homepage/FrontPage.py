import flask
from frontend import app

@app.route("/")
def frontpage():
    return flask.render_template("homepage/index.html")


