from weibo import Client

APP_KEY = '1521216146' # app key
APP_SECRET = '212c28b62505183820922d0f4f45e327' # app secret
CALLBACK_URL = 'http://heisaman.xyz/callback' # callback url

token = {u'access_token': u'2.001psIGCSorweBd556e626159iQzBB', u'remind_in': u'157679999', u'uid': u'1923041062', u'expires_at': 1629809571}
c = Client(APP_KEY, APP_SECRET, CALLBACK_URL, token=token)

res = c.get('statuses/bilateral_timeline')
print("{0}".format(res))
