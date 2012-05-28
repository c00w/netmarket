from frontend.user import login_manager
import frontend.riak

class User():
    def __init__(self, data):
        self.data = data

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False 

    def get_id(self):
        return unicode(self.data)

@login_manager.user_loader
def load_user(userid):
    user = frontend.riak.get('user', str(userid))
    if user is None:
        return None
    return User(user)
