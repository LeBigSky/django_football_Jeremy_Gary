from django import forms
from django_countries.fields import CountryField
from .models import Joueur, Equipe, Role, Continent
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.widgets import CountrySelectWidget


class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        exclude = ('moyenne',)
        widgets = {
            'country_of_origin': CountrySelectWidget(attrs={'class': 'form-select'}),
        }
        

    first_name = forms.CharField(
        label='Prénom',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    age = forms.IntegerField(
        label='Âge',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    telephone = forms.CharField(
        label='Téléphone',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    gender = forms.ChoiceField(
        label='Genre',
        choices=Joueur.GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    current_image = forms.CharField(
        label='Image actuelle',
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=False
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.image:
            self.fields['current_image'].initial = self.instance.image.name
            
    image = forms.ImageField(
        label='Image',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    role = forms.ModelChoiceField(
        label='Rôle',
        queryset=Role.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    equipe = forms.ModelChoiceField(
        label='Équipe',
        queryset=Equipe.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    vitesse = forms.IntegerField(
        label='Vitesse',
        validators=[MinValueValidator(30), MaxValueValidator(99)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    tir = forms.IntegerField(
        label='Tir',
        validators=[MinValueValidator(30), MaxValueValidator(99)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    passes = forms.IntegerField(
        label='Passes',
        validators=[MinValueValidator(30), MaxValueValidator(99)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    physique = forms.IntegerField(
        label='Physique',
        validators=[MinValueValidator(30), MaxValueValidator(99)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    defense = forms.IntegerField(
        label='Défense',
        validators=[MinValueValidator(30), MaxValueValidator(99)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    dribble = forms.IntegerField(
        label='Dribble',
        validators=[MinValueValidator(30), MaxValueValidator(99)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        exclude = ('max_players',)
        widgets = {
            'country': CountrySelectWidget(attrs={'class': 'form-select'}),
        }

    name = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    current_image = forms.CharField(
        label='Image actuelle',
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=False
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.image:
            self.fields['current_image'].initial = self.instance.image.name

    image = forms.ImageField(
        label='Image',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    
    continent = forms.ModelChoiceField(
        label='Continent',
        queryset=Continent.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    man = forms.BooleanField(
        label='Homme',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    woman = forms.BooleanField(
        label='Femme',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


    def clean(self):
        cleaned_data = super().clean()
        man = cleaned_data.get('man')
        woman = cleaned_data.get('woman')

        if not man and not woman:
            raise forms.ValidationError("Veuillez sélectionner au moins une option : homme ou femme.")

        if man and woman:
            raise forms.ValidationError("Veuillez sélectionner une seule option : homme ou femme.")