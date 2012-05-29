from xhpy.pylib import *

from django.conf import settings

class :ui:img(:x:element):
    attribute string path
    def render(self):
        path = self.getAttribute('path')
        return <img src={settings.STATIC_URL + 'img/' + path} />
