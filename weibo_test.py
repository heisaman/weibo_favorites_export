from weibo import Client

APP_KEY = '1521216146' # app key
APP_SECRET = '212c28b62505183820922d0f4f45e327' # app secret
CALLBACK_URL = 'http://heisaman.xyz/callback' # callback url

c = Client(APP_KEY, APP_SECRET, CALLBACK_URL)
print c.authorize_url
"""
c.set_code('3e96eb50a8a19fbc0cf0aa0423fb8601')
token = c.token
print token
# {u'access_token': u'2.001psIGCSorweBd556e626159iQzBB', u'remind_in': u'157679999', u'uid': u'1923041062', u'expires_at': 1629809571}

c2 = Client(APP_KEY, APP_SECRET, CALLBACK_URL, token)
c2.get('users/show', uid=2703275934)
c2.get('account/rate_limit_status')
c2.get('favorites')
"""
