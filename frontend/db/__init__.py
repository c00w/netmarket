import boto.dynamodb.layer2
from boto.dynamodb.item import Item
from boto.dynamodb.exceptions import DynamoDBKeyNotFoundError
from time import time

from frontend.configuration import AWS_ACCESS_KEY, AWS_SECRET_KEY

conn = None

def __patch():
    global conn
    if conn == None:
        conn = boto.dynamodb.layer2.Layer2(AWS_ACCESS_KEY, AWS_SECRET_KEY) 

def delete_item(table, name, value):
    conn.delete_item(Item(conn.get_table(table), hash_key = name, attrs={'value':value}))

def set_item(table, name, value, expected=False):
   __patch()
   conn.put_item(Item(conn.get_table(table), hash_key = name, attrs={'value':value}), expected_value=expected)

def get_item(table, name):
    __patch()
    try:
        t = time()
        item = conn.get_item(conn.get_table(table), name)
        e = time()
        print 'Get Time Elapsed %s' % str(e-t)
    except DynamoDBKeyNotFoundError:
        return None
    return item['value']
