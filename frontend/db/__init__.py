import boto.dynamodb.layer2
from boto.dynamodb.item import Item
from boto.dynamodb.exceptions import DynamoDBKeyNotFoundError
conn = None

_access_key ="AKIAISWIGXPF3C2L47LA"
_secret_key = "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"

def __patch():
    global conn
    if conn == None:
        conn = boto.dynamodb.layer2.Layer2(_access_key, _secret_key) 

def set_item(table, name, value):
   __patch()
   conn.put_item(Item(conn.get_table(table), hash_key = name, attrs={'value':value}))

def get_item(table, name):
    __patch()
    try:
        item = conn.get_item(conn.get_table(table), name)
    except DynamoDBKeyNotFoundError:
        return None
    return item['value']
