from django.shortcuts import render

n64games = [
    {'title': 'Super Mario 64', 'releaseyear': 1996, 'description': 'One of the greatest games ever made', 'genre' : 'adventure'},
    {'title': 'Banjo-Kazooie', 'releaseyear': 1998, 'description': 'very fun bear with a bird in his backpack', 'genre' : 'adventure'},
]

# Create your views here.

def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def n64games_index(request):
    return render(request, 'n64games/index.html', {
        'n64games': n64games
    })