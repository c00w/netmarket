from frontend.user import login_manager
import frontend.db

try:
    import simplejson as json
except:
    import json

class User():
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.from_json(args[0])
        else:
            self.username = args[0]
            self.hashpass = args[1]
            self.salt = args[2]

    def from_json(self, json_self):
        json_self = json.loads(json_self)
        self.username = json_self['Username'].decode("utf-8")
        self.hashpass = json_self['Password'].decode("utf-8")
        self.salt = json_self['Salt'].decode("hex")

    def json(self):
        return json.dumps({ 'Username':self.username.encode("utf-8"),
                 'Password':self.hashpass.encode("utf-8"),
                 'Salt':self.salt.encode("hex")})
    
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
    user = frontend.db.get_item('Users', unicode(userid))
    if user is None:
        return None
    return User(user)
