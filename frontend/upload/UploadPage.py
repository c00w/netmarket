import flask
from frontend import app

@app.route("/upload", methods=['GET', 'POST'])
def UploadPage():

    print flask.request.form
    print flask.request.files
    return flask.render_template('upload/upload.html')
