from xhpy.pylib import *
from foo.ui.js import :ui:js
from foo.ui.img import :ui:img

class :ui:service(:x:element):
    attribute string service
    def render(self):
        service = self.getAttribute('service')
        return \
        <span id="service">
            <ui:img path={service + ".png"} />
        </span>

class :ui:services(:x:element):
    attribute list services
    def render(self):
        services = self.getAttribute('services')
        services_div = <div id="services" />
        for service in services:
            services_div.appendChild(<ui:service service={service} />)
        return services_div
