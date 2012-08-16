from frontend import app
from frontend.configuration import FILE_BUCKET_NAME
from frontend.db import set_item, get_item
from frontend.page_util import has_fields
from frontend.s3 import save_file
import flask
from flask.ext.login import login_required, current_user
import hashlib
import simplejson as json

@app.route("/upload/create", methods=['GET', 'POST'])
@login_required
def upload_create():
    if has_fields(flask.request.form, ('Name', 'Category', 'Description', 'Cost')):
        name = flask.request.form['Name']
        category = flask.request.form['Category']
        description = flask.request.form['Description']
        cost = flask.request.form['Cost']
        m = hashlib.md5()
        m.update(name + category + description + cost + current_user.username)
        file_id = int(m.hexdigest(), 16)
        set_item(FILE_BUCKET_NAME, str(file_id), json.dumps({'user':current_user.username, 'file_id': file_id, 'name':name, 'category':category, 'description':description, 'cost':cost}))
        current_user.files.append(file_id)
        current_user.save_to_db()
        return flask.redirect('/upload/upload/%s' % file_id)
    return flask.render_template("upload/create.html")

@app.route("/upload/upload/<int:file_id>", methods=['GET', 'POST'])
@login_required
def upload_upload(file_id):
    print flask.request.files
    if 'data' in flask.request.files:
        print flask.request.files['data']
        key = str(file_id)
        save_file(key, flask.request.files['data'])
        return flask.redirect('/files')

    return flask.render_template("upload/upload.html", file_id=file_id)
