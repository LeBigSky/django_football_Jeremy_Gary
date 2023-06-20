from django.db import models
import uuid
import os

# ________________________________________________   // fonctions utilitaires //  ____________________________________________________________

def generate_unique_filename(instance, filename): 
    extension = filename.split('.')[-1] #j'isole l'extension du reste -> pour préserver le bon format
    unique_filename = f"{uuid.uuid4().hex}.{extension}" #je génère un nom unique que j'ajoute a {extension} -> new nom du fichier
    model_name = instance.__class__.__name__.lower() #récupère le nom de l'instance modele en minuscule -> dossier du store
    return os.path.join(model_name, unique_filename) #pathjoin join les éléments en path(chemin: model_name/unqiuefilename.extension) -> db

#_____________________________________________________________________________________________________________________________________________

