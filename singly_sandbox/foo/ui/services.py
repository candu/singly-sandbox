from xhpy.pylib import *
from foo.ui.js import :ui:js
from foo.ui.img import :ui:img

class :ui:service(:x:element):
    attribute string service @required,
              list profiles = []
    def render(self):
        service = self.getAttribute('service')
        profiles = self.getAttribute('profiles')
        link_span = \
        <span class="service-link">
            <a href={'/auth/{0}'.format(service)}>
                <ui:img path={service + ".png"} />
            </a>
        </span>
        profiles_span = <span class="service-profiles" />
        if profiles:
            link_span.addClass('already-authed')
            for profile in profiles:
                profile_span = \
                <span class="service-profile">
                    {profile}
                </span>
                profiles_span.appendChild(profile_span)
        return \
        <div class="service">
            {link_span}
            {profiles_span}
        </div>

class :ui:services(:x:element):
    attribute list services @required,
              dict profiles = {}
    def render(self):
        services = self.getAttribute('services')
        profiles = self.getAttribute('profiles')
        services_div = <div class="services" />
        for service in services:
            service_profiles = profiles.get(service, [])
            services_div.appendChild(<ui:service service={service} profiles={service_profiles} />)
        return services_div
