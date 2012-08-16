from frontend.configuration import USER_BUCKET_NAME
from frontend.user import login_manager
import frontend.db

try:
    import simplejson as json
except:
    import json

class User():
    @classmethod
    def get_user(cls, name):
        user_json = frontend.db.get_item(USER_BUCKET_NAME, name.encode("utf-8"))
        if user_json is None:
            return None
        return User(user_json)

    def save_to_db(self):
        frontend.db.set_item(USER_BUCKET_NAME, self.username.encode("utf-8"), self.json(), self.old_json)

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.from_json(args[0])
        else:
            self.username = args[0]
            self.hashpass = args[1]
            self.files = []
            self.old_json = False

    def from_json(self, json_self):
        self.old_json = json_self
        json_self = json.loads(json_self)
        self.username = json_self['Username'].decode("utf-8")
        self.hashpass = json_self['Password'].decode("utf-8")
        self.files = json_self.get('Files', [])

    def json(self):
        return json.dumps({ 'Username':self.username.encode("utf-8"),
                 'Password':self.hashpass.encode("utf-8"),
                 'Files':self.files})

    def get_files(self):
        return self.files
    
    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False 

    def get_id(self):
        return unicode(self.username)

@login_manager.user_loader
def load_user(userid):
    user = User.get_user(userid) 
    return user
