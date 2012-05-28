from frontend import app
from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.setup_app(app)

import UserPage
import User
