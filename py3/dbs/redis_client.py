# coding=utf-8
import redis


r = redis.Redis(host='localhost', port=6379, password='QqcK^JBwF3Ds', db=0)
all_keys = r.keys()
keys_to_del = [k for k in all_keys if k.startswith(b'http_')]
print(f'deleting {len(keys_to_del)} keys...')
r.delete(*keys_to_del)
print('job done')
