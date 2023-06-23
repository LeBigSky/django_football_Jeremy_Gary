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



#///////////  U R L   -->   Backend /////////////////////////////
    path('backend/', views.backhome, name="back"),
    path('player/create/', views.createJoueur, name="create_joueur"),
    path('team/create/', views.createTeam, name="create_team"),
    path('player/<int:id>', views.player, name="show_player"),
    path('team/<int:id>', views.team, name="show_team")
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
