from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Room
from .models import *
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "landing.html")


@login_required(login_url="login")
def lobby(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Room(request.POST)
        # check whether it's valid:
        if form.is_valid():
            room_choice = form.cleaned_data.get("room_choice")
            room_code = form.cleaned_data.get("room_code")
            username = request.user.username
            # Logic if the user has a room code or not to join
            if room_choice == "Create Room":
                game = Game(game_creator=username, room_code=room_code)
                game.save()
                return redirect(f'/play/{room_code}?username={username}')
            else:
                game = Game.objects.filter(room_code=room_code).first()
                print(game, request.user)
                if game is None:
                    messages.success(request, "Room Code Not Found")
                    return redirect("lobby")
                if game.is_over:
                    messages.success(request, "Sorry, the game is over.")
                    return redirect("lobby")
                game.game_opponent = username
                game.save()
                return redirect(f'/play/{room_code}?username={username}')

    else:
        form = Room()
    return render(request, "lobby.html", {'form': form})


def play(request, room_code):
    print(room_code)
    username = request.GET.get("username")
    context = {"room_code": room_code, "username": username}
    return render(request, "play.html", context)