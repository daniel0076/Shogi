from django.conf.urls import url
from channels.routing import URLRouter

import Shogi.Gateway

application = URLRouter([
    url(r"^ws/$", Shogi.Gateway.Gateway),
])
