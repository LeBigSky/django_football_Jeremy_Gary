from django.shortcuts import render, redirect
from .models import Joueur, Continent, Equipe, Role
from .forms import JoueurForm, EquipeForm


# Create your views here.
def home(request):
    joueurs= Joueur.objects.all()
    form= JoueurForm(request.POST)
    return render(request, "app/home.html")




# /////////////////////////////// BACKEND  /////////////////////////

def createJoueur(request):
     if request.method == 'POST':
        form = JoueurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
     context=locals()
     return render(request, "backend/players/create.html", context)