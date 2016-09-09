from weibo import Client
from pymongo import MongoClient
from subprocess import call

client = MongoClient()
db = client['weibo']
collection = db['favorites']

APP_KEY = '1521216146' # app key
APP_SECRET = '212c28b62505183820922d0f4f45e327' # app secret
CALLBACK_URL = 'http://heisaman.xyz/callback' # callback url
try:
    c = Client(APP_KEY, APP_SECRET, CALLBACK_URL)
    # print c.authorize_url

    c.set_code('da4f83eb1fba7f395218abdb039fbd0a')
    token = c.token
    # print token
    # {u'access_token': u'2.001psIGCSorweBd556e626159iQzBB', u'remind_in': u'157679999', u'uid': u'1923041062', u'expires_at': 1629809571}

    c2 = Client(APP_KEY, APP_SECRET, CALLBACK_URL, token)
    favorites_total_number = c2.get('favorites/ids',count=1)['total_number']

    for i in range(favorites_total_number / 500 + 1):
        res = c2.get('favorites', count=500, page=i+1)
        for favorite in res['favorites']:
            if collection.find({"_id": favorite['status']['id']}).count() > 0:
                pass
            else:
                favorite['_id'] = favorite['status']['id']
                collection.save(favorite)
except Exception as e:
    print str(e)
