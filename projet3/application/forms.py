from django import forms
from django_countries.fields import CountryField
from .models import Joueur, Equipe
from django_countries.widgets import CountrySelectWidget


class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = '__all__'
        exclude = ('moyenne',)
        widgets = {
            'country_of_origin': CountrySelectWidget(),
        }

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = '__all__'
        exclude = ('max_players',)
        widgets = {
            'country': CountrySelectWidget(),
        }