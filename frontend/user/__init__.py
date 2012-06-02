from frontend import app
from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "/login"

def logged_in():
    return flaskext.login.current_user.is_authenticated()

import UserPage
import UserClass
