from django.conf.urls import url
import Shogi.Gateway
from channels.routing import URLRouter
#from channels.routing import ProtocolTypeRouter

#application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
#})
application = URLRouter([
    url(r"^ws/$", Shogi.Gateway.Gateway),
])
