from frontend import app
from flaskext.login import LoginManager

login_manager = LoginManager()
login_manager.setup_app(app)

import user
