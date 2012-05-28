from xhpy.pylib import *

from django.http import HttpResponse

def home(request):
    page = \
    <div>
        <h1>It works</h1>
        <h2>{__name__}</h2>
    </div>
    return HttpResponse(unicode(page))
