from frontend.configuration import FILE_BUCKET_NAME
import frontend.db

import simplejson as json

class File():

    @classmethod
    def key(cls, owner, name):
        return '__'.join([owner, name])

    @classmethod
    def get_file(cls, owner, name):
        file_json = frontend.db.get_item(FILE_BUCKET_NAME, File.key(owner, name)) 
        if file_json is None:
            return None
        return File(file_json)

    def save_to_db(self):
        frontend.db.set_item(FILE_BUCKET_NAME, File.key(self.owner.encode("utf-8"), self.name.encode("utf-8")), self.json())

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.from_json(args[0])
        else:
            self.name = args[0]
            self.filename = args[1]
            self.category= args[2]
            self.description = args[3]
            self.cost = args[4]
            self.owner = args[5]

    def from_json(self, json_self):
        self.name = json_self['Name'].decode("utf-8")
        self.filename = json_self['Filename'].decode("utf-8")
        self.category = json_self['Category'].decode("utf-8")
        self.description = json_self['Description'].decode("utf-8")
        self.cost = int(json_self['Cost'])
        self.owner = json_self['Owner'].decode("utf-8")

    def json(self):
        return json.dumps({
                'Name': self.name.encode("utf-8"),
                'Filename': self.filename.encode("utf-8"),
                'Category': self.category.encode("utf-8"),
                'Description': self.description.encode("utf-8"),
                'Cost': self.cost,
                'Owner': self.owner})

