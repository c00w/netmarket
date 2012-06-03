from frontend.user import login_manager
import frontend.db

try:
    import simplejson as json
except:
    import json

class User():
    @classmethod
    def get_user(cls, name):
        user_json = frontend.db.get_item('Users', name.encode("utf-8"))
        if user_json is None:
            return None
        return User(user_json)

    def save_to_db(self):
        frontend.db.set_item('Users', self.username.encode("utf-8"), self.json(), self.old_json)

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.from_json(args[0])
        else:
            self.username = args[0]
            self.hashpass = args[1]
            self.salt = args[2]
            self.files = []
            self.old_json = False

    def from_json(self, json_self):
        self.old_json = json_self
        json_self = json.loads(json_self)
        self.username = json_self['Username'].decode("utf-8")
        self.hashpass = json_self['Password'].decode("utf-8")
        self.files = json_self.get('Files', [])
        self.salt = json_self['Salt'].decode("hex")

    def json(self):
        return json.dumps({ 'Username':self.username.encode("utf-8"),
                 'Password':self.hashpass.encode("utf-8"),
                 'Salt':self.salt.encode("hex"),
                 'Files':json.dumps(self.files)})
    
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
