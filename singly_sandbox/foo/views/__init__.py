from xhpy.pylib import *

from django.http import HttpResponse
from django.shortcuts import redirect

from foo.lib.singly import Singly

def home(request):
    if request.session.get('access_token') is None:
        return redirect('/login')
    page = \
    <div>
        <h1>It works</h1>
        <h2>{__name__}</h2>
        <h3>{request.session['access_token']}</h3>
    </div>
    return HttpResponse(unicode(page))

def login(request):
    if request.session.get('access_token') is not None:
        return redirect('/')
    return redirect(Singly.get_auth_url('facebook'))

def logout(request):
    if request.session.get('access_token') is not None:
        del request.session['access_token']
    return HttpResponse('logged out.')

def callback(request):
    if request.session.get('access_token') is not None:
        return redirect('/')
    code = request.GET.get('code')
    access_token = Singly.get_access_token(code)
    if access_token is None:
        raise Exception('access_token missing in callback response!')
    request.session['access_token'] = access_token
    return redirect('/')
