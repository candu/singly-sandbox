import httplib
import json
import urllib

from django.conf import settings

class Singly(object):
    """
    Manages OAuth flow with the various services via Singly.
    """

    API_HOST = 'api.singly.com'

    AUTH_URL = 'https://{0}/oauth/authorize'.format(API_HOST)
    ACCESS_TOKEN_URL = 'https://{0}/oauth/access_token'.format(API_HOST)

    @classmethod
    def get_auth_url(cls, service):
        params = {
            'client_id': settings.SINGLY_APP_ID,
            'redirect_uri': 'http://localhost:8000/callback',
            'service': service
        }
        return '{0}?{1}'.format(cls.AUTH_URL, urllib.urlencode(params))

    @classmethod
    def get_access_token(cls, code):
        params = urllib.urlencode({
            'client_id': settings.SINGLY_APP_ID,
            'client_secret': settings.SINGLY_APP_SECRET,
            'code': code
        })
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/plain'
        }
        conn = httplib.HTTPSConnection(cls.API_HOST)
        conn.request('POST', cls.ACCESS_TOKEN_URL, params, headers)
        resp = conn.getresponse()
        if resp.status != 200:
            raise Exception('HTTP {0} {1}'.format(resp.status, resp.reason))
        data = json.loads(resp.read())
        conn.close()
        return data.get('access_token')

    @classmethod
    def request(cls, access_token, url):
        params = {
            'access_token': access_token
        }
        full_url = '{0}?{1}'.format(url, urllib.urlencode(params))
        conn = httplib.HTTPSConnection(cls.API_HOST)
        conn.request('GET', full_url)
        resp = conn.getresponse()
        if resp.status != 200:
            raise Exception('HTTP {0} {1}'.format(resp.status, resp.reason))
        data = resp.read()
        conn.close()
        return data
