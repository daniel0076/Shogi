from django.conf.urls import url
from channels.routing import URLRouter

import Shogi_app.Gateway

application = URLRouter([
    url(r"^ws/$", Shogi_app.Gateway.Gateway),
])
