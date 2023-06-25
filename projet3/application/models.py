from django.db import models
import uuid
import os
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator


# ________________________________________________   // fonctions utilitaires //  ____________________________________________________________

def generate_unique_filename(instance, filename): 
    extension = filename.split('.')[-1] #j'isole l'extension du reste -> pour préserver le bon format
    unique_filename = f"{uuid.uuid4().hex}.{extension}" #je génère un nom unique que j'ajoute a {extension} -> new nom du fichier
    model_name = instance.__class__.__name__.lower() #récupère le nom de l'instance modele en minuscule -> dossier du store
    return os.path.join(model_name, unique_filename) #pathjoin join les éléments en path(chemin: model_name/unqiuefilename.extension) -> db

#_____________________________________________________________________________________________________________________________________________


class Continent(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    POSITION_CHOICES = [
        ('att', 'Attaquant'),
        ('mid', 'Milieu'),
        ('def', 'Défenseur'),
        ('gk', 'Gardien'),
        ('sub', 'Remplaçant'),
    ]

    position = models.CharField(max_length=10, choices=POSITION_CHOICES)

    def __str__(self):
        return self.position

class Equipe(models.Model):
    name = models.CharField(max_length=100)
    max_players = models.PositiveIntegerField(default=14)
    country = CountryField(max_length=100, countries_flag_url="https://www.worldatlas.com/r/w425/img/flag/{code}-flag.jpg")
    image = models.ImageField(upload_to=generate_unique_filename)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    man= models.BooleanField(null=True)
    woman= models.BooleanField(null=True)

    def __str__(self):
        return self.name

class Joueur(models.Model):
    GENDER_CHOICES = [
        ('M', 'Homme'),
        ('F', 'Femme'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    telephone = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country_of_origin = CountryField(countries_flag_url="https://www.worldatlas.com/r/w425/img/flag/{code}-flag.jpg")
    image = models.ImageField(upload_to=generate_unique_filename)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, default=None, null=True, blank=True)
    vitesse = models.PositiveIntegerField(
        validators=[MinValueValidator(30), MaxValueValidator(99)]
    )
    tir = models.PositiveIntegerField(
        validators=[MinValueValidator(30), MaxValueValidator(99)]
    )
    passes = models.PositiveIntegerField(
        validators=[MinValueValidator(30), MaxValueValidator(99)]
    )
    physique = models.PositiveIntegerField(
        validators=[MinValueValidator(30), MaxValueValidator(99)]
    )
    defense = models.PositiveIntegerField(
        validators=[MinValueValidator(30), MaxValueValidator(99)]
    )
    dribble = models.PositiveIntegerField(
        validators=[MinValueValidator(30), MaxValueValidator(99)]
    )
    moyenne = models.PositiveIntegerField(null=True, 
        validators=[MinValueValidator(30), MaxValueValidator(99)]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"