from frontend import app
import flask

@app.route("/files")
def files():
    return flask.render_template("files/files.html")
