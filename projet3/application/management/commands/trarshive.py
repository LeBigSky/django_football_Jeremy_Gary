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
        afro = Continent.objects.get(name='Afrique')
        usa =Continent.objects.get(name='Amérique')
        ocean =Continent.objects.get(name='Océanie')
        asia =Continent.objects.get(name='Asie')
        
        equipe_data = [
            {
                'name': 'Real Madrid',
                'max_players': 14,
                'country': 'Espagne',
                'image': 'equipe/real_madrid.png',
                'continent': euro,
                'man': 1,
                'woman': 0,

            },
            {
                'name': 'Manchester City',
                'max_players': 14,
                'country': 'Angleterre',
                'image': 'equipe/Manchester_City.png',
                'continent': euro,
                'man': True,
                'woman': False,
             
            },
            {
                'name': 'Bayern de Munich',
                'max_players': 14,
                'country': 'Allemagne',
                'image': 'equipe/bayern.png',
                'continent': euro,
                'man': '1',
                'woman': '0',
               
            },
            {
                'name': 'PSG',
                'max_players': 14,
                'country': 'France',
                'image': 'equipe/psg.png',
                'continent': euro,
                'man': True,
                'woman': False,
            },
            {
                'name': 'Club de Brugge',
                'max_players': 14,
                'country': 'Belgique',
                'image': 'equipe/brugge.png',
                'continent': euro,
                'man': True,
                'woman': False,

            },
            {
                'name': 'Tout Puissant Mazembe',
                'max_players': 14,
                'country': 'Congo Rdc',
                'image': 'equipe/mazembe.png',
                'continent': afro,
                'man': True,
                'woman': True,

            },
            {
                'name': 'Sydney FC',
                'max_players': 14,
                'country': 'Australie',
                'image': 'equipe/sydney.png',
                'continent': afro,
                'man': False,
                'woman': True,
            },
            {
                'name': 'FC Tokyo',
                'max_players': 14,
                'country': 'Japon',
                'image': 'equipe/tokyo.png',
                'continent': asia,
                'man': False,
                'woman': True,
            },
            {
                'name': 'Inter Miami',
                'max_players': 14,
                'country': 'USA',
                'image': 'equipe/miami.png',
                'continent': usa,
                'man': False,
                'woman': True,
            },
            {
                'name': 'Athletic Wydad Casablanca',
                'max_players': 14,
                'country': 'Maroc',
                'image': 'equipe/wydad.png',
                'continent': afro,
                'man': True,
                'woman': True,
            },
            {
                'name': 'Delhi United FC',
                'max_players': 14,
                'country': 'Inde',
                'image': 'equipe/delhi.png',
                'continent': asia,
                'man': True,
                'woman': True,
            },
                       {
                'name': 'Santos FC',
                'max_players': 14,
                'country': 'Brésil',
                'image': 'equipe/santos.png',
                'continent': usa,
                'man': False,
                'woman': True,
            },
                       {
                'name': 'Auckland United FC',
                'max_players': 14,
                'country': 'Nouvelle Zeelande',
                'image': 'equipe/auckland.png',
                'continent': ocean,
                'man': True,
                'woman': False,
            },
        ]

        for data in equipe_data:
            equipe = Equipe.objects.create(
                name=data['name'],
                max_players=data['max_players'],
                country=data['country'],
                continent=data['continent'],
                image=data['image'],
                man=data['man'],
                woman=data['woman']

            )

            self.stdout.write(self.style.SUCCESS('Equipe data seeded successfully.'))

            noms = [
            'Lopez', 'Garcia', 'Martinez', 'Perez', 'Rodriguez', 'Sanchez',
            'Gonzalez', 'Ramirez', 'Torres', 'Fernandez', 'Rivera', 'Diaz', 'Messi', "Mbappé", "Walker", "Friedman", "Schneizer", "Torress", "Kompany", "Kaka", "Vermeulen" , "Vertongen", "Debruyn", "Dida", "Zidane", "Mbamo" , "Nzangi", "Chong-zi", "Ponsi" , "Leblanc", "Lenoir", "Petit", "Lizarazu", "Karembeu", "Tomsha", 'Monkey-D', 'Federre', 'Ferrero','Salah','Hazard','Modric','Pogba','Aguero','De Bruyne','Ramos','Suarez','Lewandowski','Van Dijk','Griezmann',
            
        ]

        prenoms = [
            'Antonio', 'Juan', 'Manuel', 'Javier', 'Jose', 'Francisco',
            'Carlos', 'Pedro', 'Pablo', 'Alejandro', 'Luis', 'Miguel', 'Hector', 'Jean-Claude', 'Jeremy', 'Gary', 'Denzel', 'Quentin', 'Adil', 'Wadoud', 'Kadri', 'José', 'Christian', 'Kevin', 'Nicolas', 'Yuri', 'Viktor', 'Bienveillance', 'Bijou', 'Mamadou', 'Dieu-Soit-Loué', 'Béni', 'Yang', 'Gohan', 'Luffy','Lionel','Cristiano','Kylian','Neymar','Mohamed',
          
        ]
        prenoms_filles = [
            'Anna', 'Juanita', 'Manuela', 'Jajita', 'Josianne', 'Francoise',
            'Carla', 'Petra', 'Paola', 'Alejandra', 'Luisa', 'Michelle', 'Helène', 'Jeanne', 'Olivia', 'Gabrielle', 'Denza', 'Queen', 'Amal', 'Jamila', 'Kadrina', 'Katrina', 'Cristiana', 'Kelly', 'Nicole', 'Yumiko', 'Viktoria', 'Bienveillée', 'Electra', 'Mamasita', 'Sanaé', 'Benjamine', 'Itsuko', 'Chichi', 'Loulou', "Patricia", "Enide", "Charlotte", "Fadia", "Pamela", "Claudia",'Marta','Alex','Ada','Megan','Sam',
         
        ]

        joueurs_images = [
            'joueur/joueur-{}.png'.format(i+1) for i in range(46)
        ]
        femmes_images =[
            'femmes/joueuse-{}.png'.format(i+1) for i in range(23)
        ]
        

        # Limites pour chaque rôle
        max_attaquants = 3
        max_defenseurs = 5
        max_milieux = 3
        max_gardiens = 2
        max_remplacants = 3



           
            # self.stdout.write(self.style.SUCCESS(f'Joueur {joueur.first_name} {joueur.last_name} créé.'))
        for i in range(100):  # Ajouter 40 joueurs
             role = Role.objects.order_by('?').first()

             gender_choices =['M', 'F']
             gender = random.choices(gender_choices)[0]
    # Choisir une équipe au hasard
             if gender == 'M':
                    equipe_choices = [equipe for equipe in Equipe.objects.filter(man=True)] + [None]
                    equipe = random.choice(equipe_choices)
             if gender == 'F':
                    equipe_choices = [equipe for equipe in Equipe.objects.filter(woman=True)] + [None]
                    equipe = random.choice(equipe_choices)

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
             if gender == 'F':
                prenom = random.choice(prenoms_filles)
                image = random.choice(femmes_images)
             else:
                prenom = random.choice(prenoms)
                image = random.choice(joueurs_images)

             joueur = Joueur.objects.create(
                    first_name=prenom,
                    last_name=nom,
                    age=random.randint(18, 38),
                    telephone=str(random.randint(10000000, 99999999)),
                    email = f'{nom.lower()}.{prenom.lower()}@{equipe.name.replace(" ", "").lower()}.com' if equipe else f'{nom.lower()}.{prenom.lower()}@lebanc.com',
                    gender=gender,
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
                    moyenne=0  # À définir selon tes critères
                )

             self.stdout.write(self.style.SUCCESS(f'Joueur {joueur.first_name} {joueur.last_name} créé.'))
