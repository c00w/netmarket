import flask
from frontend import app
from frontend.page_util import has_fields

@app.route("/upload/upload", methods=['GET', 'POST'])
def UploadPage():

    if 'data' in flask.request.files:
        print flask.request.files['data']  
    return flask.render_template('upload/upload.html')

