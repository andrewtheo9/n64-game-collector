from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import N64game
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
    session_form = SessionForm()
    return render(request, 'n64games/detail.html', { 'n64game': n64game, 'session_form': session_form})

class N64gameCreate(CreateView):
    model = N64game
    fields = '__all__'
    success_url = '/n64games/{n64game_id}'

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