from django.shortcuts import render, redirect
from .models import Joueur, Continent, Equipe, Role
from .forms import JoueurForm, EquipeForm
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
    hommes_avec_equipe = joueurs.filter(gender='M', equipe_id__isnull=False)[:5]

    context = locals()
    return render(request, "app/home.html", context)




# /////////////////////////////// BACKEND  /////////////////////////

def createJoueur(request):
     if request.method == 'POST':
        form = JoueurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
     context=locals()
     return render(request, "backend/players/create.html", context)