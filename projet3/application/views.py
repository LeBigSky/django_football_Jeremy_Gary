from django.shortcuts import render, redirect
from django.db import models
from .models import Joueur, Continent, Equipe, Role
from .forms import JoueurForm, EquipeForm
from django.contrib import messages
from django.db.models import Count


# Create your views here.
def home(request):
    joueurs = Joueur.objects.all()
    form = JoueurForm(request.POST)
    equipes = Equipe.objects.all()

    

    equipes_remplies = Equipe.objects.annotate(num_joueurs=Count('joueur')).filter(num_joueurs=14)

    equipes_non_remplies = Equipe.objects.annotate(num_joueurs=Count('joueur')).filter(num_joueurs__lt=14)[:2]

    joueurs_libres = joueurs.filter(equipe_id__isnull=True).order_by('?')[:4]
    joueurs_non_libres = joueurs.filter(equipe_id__isnull=False).order_by('?')[:4]

    equipes_euro = equipes.filter(continent_id=4)
    equipes_autre = equipes.exclude(continent_id=4)

    femmes_sans_equipe = joueurs.filter(gender='F', equipe_id__isnull=True).order_by('?')[:5]
    hommes_avec_equipe = joueurs.filter(gender='M', equipe_id__isnull=False).order_by('?')[:5]

    nb_joueurs = joueurs.count()
    nb_equipes = equipes.count()
    nb_joueurs_non_libres = joueurs.filter(equipe_id__isnull=False).count()

    context = locals()
    return render(request, "app/home.html", context)


def player(request, id):
    joueur = Joueur.objects.get(id=id)
    context = locals()
    return render(request, "app/pages/show_player.html", context)

def team(request, id):
    equipe = Equipe.objects.get(id=id)
    context = locals()
    return render(request, "app/pages/show_team.html", context)

def male_players(request):
    joueurs_hommes = Joueur.objects.all().filter(gender='M').order_by('equipe_id')
    context = locals()
    return render(request, "app/pages/male_players.html", context)

def female_players(request):
    joueurs_femmes = Joueur.objects.all().filter(gender='F')
    context = locals()
    return render(request, "app/pages/female_players.html", context)


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