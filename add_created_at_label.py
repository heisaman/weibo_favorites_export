from pymongo import MongoClient

from datetime import datetime

client = MongoClient()
db = client['weibo']
collection = db['favorites']
n = 0
for favorite in collection.find():
    created_at = datetime.strptime(favorite['status']['created_at'], "%a %b %d %H:%M:%S %z %Y")
    favorite['created_at'] = int(created_at.timestamp())
    collection.save(favorite)
    n = n + 1
    print(n)