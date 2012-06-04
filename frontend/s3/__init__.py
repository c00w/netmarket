from boto.s3.connection import S3Connection
from boto.s3.key import Key

_access_key ="AKIAISWIGXPF3C2L47LA"
_secret_key = "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"

conn = S3Connection(_access_key, _secret_key)
bucket = conn.create_bucket('netmarket_sales')

def save_file(key, fp):
    Key(bucket, key)
    Key.set_contents_from_file(fp)    
