from xhpy.pylib import *

import json

from django.http import HttpResponse
from django.shortcuts import redirect

from foo.lib.singly import Singly
from foo.ui.services import :ui:services
from foo.ui.page import :ui:page

SERVICES = [
    'email',
    'facebook',
    'fitbit',
    'foursquare',
    'gcontacts',
    'github',
    'instagram',
    'linkedin',
    'tumblr',
    'twitter',
]

def home(request):
    if request.session.get('access_token') is None:
        return redirect('/login')
    data = Singly.request(request.session['access_token'], '/profiles')
    profiles = json.loads(data)
    page = \
    <ui:page>
        <h1>Singly Sandbox</h1>
        <h2>Authenticate with the following services:</h2>
        <ui:services services={SERVICES} profiles={profiles} />
    </ui:page>
    return HttpResponse(unicode(page))

def auth(request, service):
    if service not in SERVICES:
        return redirect('/')
    return redirect(Singly.get_auth_url(service))

def logout(request):
    if request.session.get('access_token') is not None:
        del request.session['access_token']
    return HttpResponse('logged out.')

def callback(request):
    code = request.GET.get('code')
    access_token = Singly.get_access_token(code)
    if access_token is None:
        raise Exception('access_token missing in callback response!')
    request.session['access_token'] = access_token
    return redirect('/')
