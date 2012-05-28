import riak

client = riak.RiakClient(port=8091)

def get_bucket(name):
    return client.bucket(name)

def store(bucket, name, data):
    bucket = get_bucket(bucket)
    robject = bucket.new(name, data)
    robject.store()

def get(bucket, name):
    bucket = get_bucket(bucket) 
    robject = bucket.get(name)
    return robject.get_data()
