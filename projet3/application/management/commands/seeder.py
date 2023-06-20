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