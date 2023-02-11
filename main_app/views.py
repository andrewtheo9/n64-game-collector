from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import N64game, Player
from .forms import SessionForm

# Create your views here.

def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def n64games_index(request):
    n64games = N64game.objects.all()
    return render(request, 'n64games/index.html', {
        'n64games': n64games
    })

def n64games_detail(request, n64game_id):
    n64game = N64game.objects.get(id=n64game_id)
    id_list = n64game.players.all().values_list('id')
    players_n64game_doesnt_have = Player.objects.exclude(id__in=id_list)
    session_form = SessionForm()
    return render(request, 'n64games/detail.html', { 'n64game': n64game, 'session_form': session_form})

class N64gameCreate(CreateView):
    model = N64game
    fields = ['title', 'year', 'genre', 'description']
    success_url = '/n64games'

class N64gameUpdate(UpdateView):
    model = N64game
    fields = ['year', 'genre', 'description']

class N64gameDelete(DeleteView):
    model = N64game
    success_url = '/n64games'

def add_session(request, n64game_id):
    form = SessionForm(request.POST)
    if form.is_valid():
        new_session = form.save(commit=False)
        new_session.n64game_id = n64game_id
        new_session.save()
    return redirect('detail', n64game_id=n64game_id)

class PlayerList(ListView):
    model = Player

class PlayerDetail(DetailView):
    model = Player

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['number', 'name']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players'

def assoc_player(request, n64game_id, player_id):
    N64game.objects.get(id=n64game_id).players.add(player_id)
    return redirect('detail', n64game_id=n64game_id)

def remove_player(request, n64game_id, player_id):
    N64game.objects.get(id=n64game_id).players.remove(player_id)
    return redirect('detail', n64game_id=n64game_id)