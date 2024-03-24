import json
from datetime import datetime
from django.core.management.base import BaseCommand
from civicmap.models import Vigicrue, Station

def convertir_valeur_numerique(valeur):
    try:
        return float(valeur) if valeur != "" else None
    except (ValueError, TypeError):
        return None

def convertir_date(valeur):
    try:
        return datetime.strptime(valeur, "%Y-%m-%d") if valeur != "" else None
    except (ValueError, TypeError):
        return None

class Command(BaseCommand):
    help = 'Supprime les données existantes et importe les données de stations depuis un fichier JSON'

    def handle(self, *args, **kwargs):
        # Étape 1: Suppression des données existantes
        Station.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Données existantes supprimées avec succès'))

        # Étape 2: Ouverture et lecture du fichier JSON
        with open('data/init_station.json', 'r', encoding='utf-8') as json_file:
            station_data = json.load(json_file)
            for index, entry in enumerate(station_data):
                niveau_alerte, _ = Vigicrue.objects.get_or_create(
                    niveau_alerte=int(entry['niveau_alerte']),
                    defaults={'niveau_alerte': 0} 
                )
                Station.objects.create(
                    code = entry['code'],
                    nom = entry['nom'],
                    hauteur_max = convertir_valeur_numerique(entry['hauteur_max']),
                    debit_max = convertir_valeur_numerique(entry['debit_max']),
                    date_max = convertir_date(entry['date_max']),
                    riviere = entry['riviere'],
                    latitude = convertir_valeur_numerique(entry['latitude']),
                    longitude = convertir_valeur_numerique(entry['longitude']),
                    date_alerte = convertir_date(entry['date_alerte']),
                    niveau_alerte=niveau_alerte
                )
        self.stdout.write(self.style.SUCCESS('Données importées avec succès'))

