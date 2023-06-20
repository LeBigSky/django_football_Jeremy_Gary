from django import forms
from django_countries.fields import CountryField
from .models import Joueur, Equipe
from django_countries.widgets import CountrySelectWidget


class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['first_name', 'last_name', 'age', 'telephone', 'email', 'gender', 'country_of_origin', 'image', 'role', 'equipe']
        widgets = {
            'country_of_origin': CountrySelectWidget(),
        }

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['name', 'max_players', 'country', 'continent']
        widgets = {
            'country': CountrySelectWidget(),
        }