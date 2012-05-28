from frontend.user import login_manager
import frontend.riak

@login_manager.user_loader
def load_user(userid):
    user = frontend.riak.get('user', str(userid))
    if user is None:
        return None
    return User(user)

class User():
    def __init__(self, data):
        self.data = data
