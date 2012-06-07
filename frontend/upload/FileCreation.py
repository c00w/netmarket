from frontend import app
import flask

@app.route("/upload/create", methods=['GET', 'POST'])
def upload_create():
    print flask.request
    print flask.request.form
    return flask.render_template("upload/create.html")

def handle_post():
    pass
