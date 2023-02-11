from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('n64games/', views.n64games_index, name='index'),
    path('n64games/<int:n64game_id>/', views.n64games_detail, name='detail' ),
    path('n64games/create/', views.N64gameCreate.as_view(), name='n64games_create'),
    path('n64games/<int:pk>/update/', views.N64gameUpdate.as_view(), name='n64games_update'),
    path('n64games/<int:pk>/delete/', views.N64gameDelete.as_view(), name='n64games_delete'),
    path('n64games/<int:n64game_id>/add_session/', views.add_session, name='add_session'),
    path('n64games/<int:cat_id>/assoc_player/<int:player_id>/', views.assoc_player, name='assoc_player'),
    path('n64games/<int:cat_id>/remove_player/<int:player_id>/', views.remove_player, name='remove_player'),
    path('players/', views.PlayerList.as_view(), name='players_index'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='players_detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
]