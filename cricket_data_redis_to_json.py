# -*- coding: utf-8 -*
import json
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

r = redis.Redis(connection_pool=pool)
f1=open('cridata.json','wb')

for i in range(0,len(r.lrange("data:one:day:match",0,-1))):
    result=r.lpop("data:one:day:match")
    r.lpush("data:one:day:match",result)
    json.dump(result, f1)
    f1.write("\n")

# or
# ids= r.lrange('data:one:day:match', 0,-1)
# print ids
# json.dump(ids, f1)    