import flask
from frontend import app

@app.route("/upload")
def UploadPage():
    return flask.render_template('upload.html')
