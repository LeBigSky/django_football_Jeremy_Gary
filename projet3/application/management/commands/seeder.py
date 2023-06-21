import os
import random
from django.core.management.base import BaseCommand
from application.models import Joueur, Equipe, Continent, Role
from django_countries import countries
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        Role.objects.all().delete()
        Equipe.objects.all().delete()
        Continent.objects.all().delete()

        
        continents = [
            'Afrique',
            'Amérique',
            'Asie',
            'Europe',
            'Océanie',
        ]

        for continent_name in continents:
            continent, _ = Continent.objects.get_or_create(name=continent_name)
            self.stdout.write(f"Continent '{continent_name}' seeded successfully.")

        role_data =[
           { 'position': 'att'},
           { 'position': 'mid'},
            { 'position': 'def'},
            { 'position': 'gk'},
           { 'position': 'sub'},
        ]
        for roles in role_data:
          Role.objects.create(**roles)
          

        euro = Continent.objects.get(name='Europe')
        
        equipe_data = [
            {
                'name': 'Real Madrid',
                'max_players': 14,
                'country': 'Espagne',
                'image': 'equipe/real_madrid.jpg',
                'continent': euro,
            },
            {
                'name': 'Manchester City',
                'max_players': 14,
                'country': 'Angleterre',
                'image': 'equipe/Manchester-city.jpg',
                'continent': euro,
            },
            {
                'name': 'Bayern de Munich',
                'max_players': 14,
                'country': 'Allemagne',
                'image': 'equipe/Bayern.jpg',
                'continent': euro,
            },
            {
                'name': 'PSG',
                'max_players': 14,
                'country': 'France',
                'image': 'equipe/PSG.jpg',
                'continent': euro,
            },
            {
                'name': 'Club de Brugge',
                'max_players': 14,
                'country': 'Belgique',
                'image': 'equipe/Brugge.jpg',
                'continent': euro,
            },
        ]

        for data in equipe_data:
            equipe = Equipe.objects.create(
                name=data['name'],
                max_players=data['max_players'],
                country=data['country'],
                continent=data['continent'],
                image=data['image']
            )

            self.stdout.write(self.style.SUCCESS('Equipe data seeded successfully.'))

            noms = [
            'Lopez', 'Garcia', 'Martinez', 'Perez', 'Rodriguez', 'Sanchez',
            'Gonzalez', 'Ramirez', 'Torres', 'Fernandez', 'Rivera', 'Diaz', 'Messi', "Mbappé", "Walker", "Friedman", "Schneizer", "Torress", "Kompany", "Kaka", "Vermeulen" , "Vertongen", "Debruyn", "Dida", "Zidane", "Mbamo" , "Nzangi", "Chong-zi", "Ponsi" , "Leblanc", "Lenoir", "Petit", "Lizarazu", "Karembeu", "Tomsha", 'Monkey-D', 'Federre', 'Ferrero'
            # ... Ajoute les autres noms de joueurs connus ici ...
        ]

        prenoms = [
            'Antonio', 'Juan', 'Manuel', 'Javier', 'Jose', 'Francisco',
            'Carlos', 'Pedro', 'Pablo', 'Alejandro', 'Luis', 'Miguel', 'Hector', 'Jean-Claude', 'Jeremy', 'Gary', 'Denzel', 'Quentin', 'Adil', 'Wadoud', 'Kadri', 'José', 'Christian', 'Kevin', 'Nicolas', 'Yuri', 'Viktor', 'Bienveillance', 'Bijou', 'Mamadou', 'Dieu-Soit-Loué', 'Béni', 'Yang', 'Gohan', 'Luffy'
            # ... Ajoute les autres prénoms de joueurs connus ici ...
        ]

        joueurs_images = [
            'joueur/joueur-{}.png'.format(i+1) for i in range(40)
        ]

        # Limites pour chaque rôle
        max_attaquants = 3
        max_defenseurs = 5
        max_milieux = 3
        max_gardiens = 2
        max_remplacants = 3

        for i in range(40):  # Ajouter 40 joueurs
            role = Role.objects.order_by('?').first()

            # Choisir une équipe au hasard
            equipe = Equipe.objects.order_by('?').first()

            # Compter le nombre de joueurs existants dans chaque rôle pour l'équipe
            nb_attaquants = Joueur.objects.filter(equipe=equipe, role__position='att').count()
            nb_defenseurs = Joueur.objects.filter(equipe=equipe, role__position='def').count()
            nb_milieux = Joueur.objects.filter(equipe=equipe, role__position='mid').count()
            nb_gardiens = Joueur.objects.filter(equipe=equipe, role__position='gk').count()
            nb_remplacants = Joueur.objects.filter(equipe=equipe, role__position='sub').count()

            if (
                (role.position == 'att' and nb_attaquants >= max_attaquants) or
                (role.position == 'def' and nb_defenseurs >= max_defenseurs) or
                (role.position == 'mid' and nb_milieux >= max_milieux) or
                (role.position == 'gk' and nb_gardiens >= max_gardiens) or
                (role.position == 'sub' and nb_remplacants >= max_remplacants)
            ):
                # Limite atteinte pour ce rôle, passer au joueur suivant
                continue

            nom = random.choice(noms)
            prenom = random.choice(prenoms)
            image = random.choice(joueurs_images)

            joueur = Joueur.objects.create(
                first_name=prenom,
                last_name=nom,
                age=random.randint(18, 38),
                telephone=str(random.randint(10000000, 99999999)),
                email=f'{nom.lower()}.{prenom.lower()}@{equipe.name.replace(" ", "").lower()}.com',
                gender='M',  # Genre masculin
                country_of_origin=random.choice(countries),
                image=image,
                role=role,
                equipe=equipe,
                vitesse=random.randint(75, 99) if role.position == 'att' else random.randint(50, 75),
                tir=random.randint(75, 99) if role.position == 'att' else random.randint(60, 99),
                passes=random.randint(75, 99) if role.position == 'att' else random.randint(60, 99),
                physique=random.randint(75, 99) if role.position == 'att' else random.randint(60, 99),
                defense=random.randint(35, 65) if role.position == 'att' else random.randint(60, 99),
                dribble=random.randint(75, 99) if role.position == 'att' else random.randint(60, 99),
                moyenne= 0  # À définir selon tes critères
            )

            self.stdout.write(self.style.SUCCESS(f'Joueur {joueur.first_name} {joueur.last_name} créé.'))
