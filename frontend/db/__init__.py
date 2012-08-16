from time import time
from redis import StrictRedis

conn = None

def __patch():
    global conn
    if conn == None:
        conn = StrictRedis(host='localhost', port=6379, db=0)

def __key(table, name):
    return '__'.join([table, name])

def delete_item(table, name, value):
    return conn.delete(__key(table, name))

def set_item(table, name, value, expected=False):
   __patch()
   return conn.set(__key(table, name), value)

def get_item(table, name):
    __patch()
    return conn.get(__key(table, name))
