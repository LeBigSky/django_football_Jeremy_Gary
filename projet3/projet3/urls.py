from django.contrib import admin
from django.urls import path
from application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("players/male/", views.male_players, name="hommes"),
    path("players/female/", views.female_players, name="femmes"),
    path('player/<int:id>', views.player, name="show_player"),
    path('team/<int:id>', views.team, name="show_team"),
    path('male_league', views.male_league, name="male_league"),
    path('female_league', views.female_league, name="female_league"),
    path('mixte_league', views.mixte_league, name="mixte_league"),



#///////////  U R L   -->   Backend /////////////////////////////
    path('backend/', views.backhome, name="back"),
    path('player/create/', views.createJoueur, name="create_joueur"),
    path('team/create/', views.createTeam, name="create_team"),
    path('team/editor/', views.allteams, name="team_editor"),
    path('player/editor/', views.allplayers, name="player_editor"),
    path('team/update/<int:id>', views.updateTeam, name="update_team"),
    path('player/update/<int:id>', views.updatePlayer, name="update_player"),
    path('delete/team/<int:id>', views.deleteTeam, name="delete_team"),
    path('delete/player/<int:id>/', views.deletePlayer, name="delete_player")
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
