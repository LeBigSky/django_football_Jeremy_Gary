from django.shortcuts import render, redirect
from django.db import models
from .models import Joueur, Continent, Equipe, Role
from .forms import JoueurForm, EquipeForm
from django.contrib import messages
from django.db.models import Count


# Create your views here.
def home(request):
    message_list = messages.get_messages(request)
    joueurs= Joueur.objects.all()
    form= JoueurForm(request.POST)
    context=locals()
    return render(request, "app/home.html", context)



































# /////////////////////////////// BACKEND  /////////////////////////

def backhome(request):

    return render(request, "backend/home.html")

def createJoueur(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST, request.FILES)
        if form.is_valid():
            joueur = form.save(commit=False)

            # Vérification de l'équipe pleine
            if joueur.equipe.joueur_set.count() >= 14:
                messages.error(request, "L'équipe est pleine.")
                return redirect('create_joueur')
            
            equipe_man = joueur.equipe.man
            equipe_woman = joueur.equipe.woman
            joueur_gender = joueur.gender

            if equipe_man and not equipe_woman:
                if joueur_gender != 'M':
                    messages.error(request, "Désolé, le joueur doit être de genre masculin (M).")
                    return redirect('create_joueur')

            elif equipe_woman and not equipe_man:
                if joueur_gender != 'F':
                    messages.error(request, "Désolé, le joueur doit être de genre féminin (F).")
                    return redirect('create_joueur')

            joueur.save()
            messages.success(request, "Le joueur a été crée !")
            return redirect('/')
    else:
        form = JoueurForm()
    
    context = locals()
    return render(request, "backend/players/create.html", context)

def createTeam(request):
    if request.method =="POST":
        form = EquipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Bravo !, l'équipe a été ajouté.")
            return redirect('back')
        else:
            form=EquipeForm()
            return redirect("create_team")
    else:
        form = EquipeForm()    
    context = locals()
    return render(request, "backend/teams/create.html", context)