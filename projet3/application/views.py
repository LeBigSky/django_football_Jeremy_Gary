from django.shortcuts import render, redirect
from django.db import models
from .models import Joueur, Continent, Equipe, Role
from .forms import JoueurForm, EquipeForm
from django.contrib import messages
from django.db.models import Count
import os
from django.conf import settings


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
    joueurs_att = Joueur.objects.all().filter(equipe_id=id, role_id=1)
    joueurs_mid = Joueur.objects.all().filter(equipe_id=id, role_id=2)
    joueurs_def = Joueur.objects.all().filter(equipe_id=id, role_id=3)
    joueurs_gk = Joueur.objects.all().filter(equipe_id=id, role_id=4)
    joueurs_sub = Joueur.objects.all().filter(equipe_id=id, role_id=5)

    nb_joueurs = Joueur.objects.all().filter(equipe_id=id).count()
    context = locals()
    return render(request, "app/pages/show_team.html", context)

def male_players(request):
    joueurs_hommes = Joueur.objects.all().filter(gender='M').order_by('equipe_id')
    context = locals()
    return render(request, "app/pages/male_players.html", context)

def female_players(request):
    joueurs_femmes = Joueur.objects.all().filter(gender='F').order_by('equipe_id')
    context = locals()
    return render(request, "app/pages/female_players.html", context)

def male_league(request):
    equipes = Equipe.objects.all().filter(man=1, woman=0)
    context = locals()
    return render(request, "app/pages/male_league.html", context)

def female_league(request):
    equipes = Equipe.objects.all().filter(man=0, woman=1)
    context = locals()
    return render(request, "app/pages/female_league.html", context)

def mixte_league(request):
    equipes = Equipe.objects.all().filter(man=1, woman=1)
    context = locals()
    return render(request, "app/pages/mixte_league.html", context)


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
            
            joueur.moyenne = (joueur.vitesse + joueur.physique + joueur.dribble + joueur.passes + joueur.tir + joueur.defense )/6
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

def deleteTeam(request, id):
    team=Equipe.objects.get(id=id)
    team.delete()
    return redirect('team_editor')

def allteams(request):
    equipes=Equipe.objects.all()
    context=locals()
    return render(request, "backend/teams/allteams.html", context)

def updateTeam(request, id):
    team=Equipe.objects.get(id=id)
    form=EquipeForm(instance=team)
    if request.method == 'POST':
        form = EquipeForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, "Bravo !, l'équipe a été ajouté.")
            return redirect('back')  
    context= locals()
    return render(request, "backend/teams/update.html", context)

def allplayers(request):
    players=Joueur.objects.all().order_by('equipe_id')
    context=locals()
    return render(request, "backend/players/allplayers.html", context)

def deletePlayer(request, id):
     joueur = Joueur.objects.get(id=id)

    # Vérification de la longueur de l'URL de l'image
     if len(joueur.image.name) > 20:
        # Chemin complet vers l'image
        image_path = os.path.join(settings.MEDIA_ROOT, joueur.image.name)

        # Vérification si le fichier existe avant de le supprimer
        if os.path.exists(image_path):
            # Suppression du fichier
            os.remove(image_path)

     joueur.delete()
     return redirect('player_editor')

def updatePlayer(request, id):
    joueur = Joueur.objects.get(id=id)
    form = JoueurForm(instance=joueur)

    if request.method == 'POST':
        form = JoueurForm(request.POST, request.FILES, instance=joueur)
        if form.is_valid():
            equipe = form.cleaned_data['equipe']
            role = form.cleaned_data['role']
            gender = form.cleaned_data['gender']

            # Vérification de l'équipe complète, sauf pour l'équipe du joueur en cours d'édition
            if equipe.joueur_set.count() >= equipe.max_players and equipe != joueur.equipe:
                messages.error(request, "Désolé, cette équipe est déjà complète.")
                return redirect(request.META.get('HTTP_REFERER'))

            # Vérification du nombre de joueurs par rôle, sauf pour le joueur en cours d'édition
            if equipe.joueur_set.filter(role=role).count() >= 3 and joueur not in equipe.joueur_set.all():
                messages.error(request, "Désolé, plus de place pour ce rôle.")
                return redirect(request.META.get('HTTP_REFERER'))

            # Vérification du nombre de gardiens, sauf pour le joueur en cours d'édition
            if role.position == 'gk' and equipe.joueur_set.filter(role__position='gk').count() >= 2 and joueur not in equipe.joueur_set.all():
                messages.error(request, "Désolé, il y a déjà 2 gardiens dans cette équipe.")
                return redirect(request.META.get('HTTP_REFERER'))

            # Vérification du genre en fonction de l'équipe
            if equipe.man and not equipe.woman and gender != 'M':
                messages.error(request, "Le genre doit être homme pour cette équipe.")
                return redirect(request.META.get('HTTP_REFERER'))

            if equipe.woman and not equipe.man and gender != 'F':
                messages.error(request, "Le genre doit être femme pour cette équipe.")
                return redirect(request.META.get('HTTP_REFERER'))

            form.save()
            messages.success(request, "Bravo ! Le joueur a été modifié.")
            return redirect('back')

    context = locals()
    return render(request, "backend/players/update.html", context)