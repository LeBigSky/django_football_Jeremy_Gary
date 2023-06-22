from django.contrib import admin
from django.urls import path
from application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),



#///////////  U R L   -->   Backend /////////////////////////////
    path('backend/', views.backhome, name="back"),
    path('player/create/', views.createJoueur, name="create_joueur"),
    path('team/create/', views.createTeam, name="create_team")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)