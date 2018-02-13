# coding=utf-8
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('zhitong')
bucket.objects.filter(Prefix='job/comPosition')
for o in bucket.objects.filter(Prefix='job/comPosition'):
    key = o.key
    local = key[key.index('/')+1:]
    bucket.download_file(key, local)
