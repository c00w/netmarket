from frontend import app
import flask

@app.route("/settings")
def settings():
    return flask.render_template("settings/settings.html")
