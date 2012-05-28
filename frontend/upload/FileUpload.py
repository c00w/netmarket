import flask
from frontend import app

@app.route("/upload/upload", methods=['GET', 'POST'])
def UploadPage():

    return flask.render_template('upload/upload.html')
