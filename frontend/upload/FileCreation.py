from frontend import app
import flask

@app.route("/upload/create", methods=['GET', 'POST'])
def upload_create():
    return flask.render_template("upload/create.html")

def handle_post():
