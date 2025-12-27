import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")
django_asgi_app = get_asgi_application()

from conf.consumers import ChatConsumer

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": URLRouter(
            [
                re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),  # ← ЧАТ!
                re_path(r"ws/test/$", ChatConsumer.as_asgi()),  # тест оставим
            ]
        ),
    }
)
