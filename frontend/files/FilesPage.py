from frontend import app
import flask
from flask.ext.login import login_required, current_user

import simplejson as json

@app.route("/files")
@login_required
def files():
    return flask.render_template("files/files.html")

@app.route("/files/list")
@login_required
def list_files():
    files = current_user.get_files() 
    return json.dumps(files)
