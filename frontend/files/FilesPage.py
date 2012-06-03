from frontend import app
import flask
from flask.ext.login import login_required, current_user

@app.route("/files")
@login_required
def files():
    files = current_user.get_files() 
    return flask.render_template("files/files.html")
