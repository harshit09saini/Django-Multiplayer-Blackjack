from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('lobby', views.lobby, name="lobby"),
    path('play/<room_code>', views.play, name="play")
]
