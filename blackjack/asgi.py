"""
ASGI config for blackjack project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from game.consumers import GameRoom

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blackjack.settings')
django_asgi_app = get_asgi_application()
django.setup()

ws_patterns = [
    path("ws/game/<room_code>", GameRoom.as_asgi())
]

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(URLRouter(ws_patterns))
})
