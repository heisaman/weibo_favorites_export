from weibo import Client
from pymongo import MongoClient
from subprocess import call

import sys, traceback
from datetime import datetime

client = MongoClient()
db = client['weibo']
collection = db['favorites']

APP_KEY = '1521216146' # app key
APP_SECRET = '212c28b62505183820922d0f4f45e327' # app secret
CALLBACK_URL = 'http://heisaman.xyz/callback' # callback url

n = 0
try:
    token = {u'access_token': u'2.001psIGCSorweBd556e626159iQzBB', u'remind_in': u'157679999', u'uid': u'1923041062', u'expires_at': 1629809571}
    c = Client(APP_KEY, APP_SECRET, CALLBACK_URL, token=token)

    # print token
    # {u'access_token': u'2.001psIGCSorweBd556e626159iQzBB', u'remind_in': u'157679999', u'uid': u'1923041062', u'expires_at': 1629809571}
    print(c.alive)
    favorites_total_number = c.get('favorites/ids',count=1)['total_number']
    print("共收藏了微博{0}条".format(favorites_total_number))

    for i in range(favorites_total_number // 50 + 1):
        print("第{0}页".format(i+51))
        res = c.get('favorites', count=50, page=i+51)
        print("{0}条收藏".format(len(res['favorites'])))
        for favorite in res['favorites']:
            n = n + 1
            if collection.find({"_id": favorite['status']['id']}).count() > 0:
                pass
            else:
                favorite['_id'] = favorite['status']['id']
                if favorite['status']['created_at'] == '':
                    created_at = datetime.strptime('Wed Nov 28 15:00:00 +0800 2012', "%a %b %d %H:%M:%S %z %Y")
                else:
                    created_at = datetime.strptime(favorite['status']['created_at'], "%a %b %d %H:%M:%S %z %Y")
                favorite['created_at'] = round(created_at.timestamp())
                collection.save(favorite)
                print("{0}新保存, 收藏时间:{1}".format(n, favorite["favorited_time"]))
except Exception as e:
    traceback.print_exc()
