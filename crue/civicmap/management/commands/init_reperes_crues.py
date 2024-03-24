import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from civicmap.models import RepereCrue, Station

def convertir_valeur_numerique(valeur):
    try:
        return float(valeur) if valeur != "" else None
    except ValueError:
        return None

def convertir_integer(valeur):
    try:
        return int(valeur) if valeur != "" else None
    except ValueError:
        return None

def convertir_date(valeur):
    try:
        return datetime.strptime(valeur, "%d/%m/%Y") if valeur != "" else None
    except (ValueError, TypeError):
        return None

class Command(BaseCommand):
    help = 'Supprime les données existantes et importe les données de repères de crues depuis un fichier CSV'

    def handle(self, *args, **kwargs):
        # Étape 1: Suppression des données existantes
        RepereCrue.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Données existantes supprimées avec succès'))

        # Étape 2: Ouverture et lecture du fichier CSV
        with open('data/BDD.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                station, _ = Station.objects.get_or_create(
                    code=row['Code station'],
                    defaults={'nom': 'Nom inconnu'} 
                )
                RepereCrue.objects.create(
                    nom=row['Nom'],
                    id_gsheet=convertir_integer(row['ID']),
                    latitude=convertir_valeur_numerique(row.get('Latitude')),
                    longitude=convertir_valeur_numerique(row.get('Longitude')),
                    adresse=row.get('Adresse'),
                    code_station=station,
                    date=convertir_date(row.get('Date')),
                    presentation_crue=row.get('Présentation de la crue'),
                    contexte=row.get('Contexte'),
                    impact_humain_urbain=row.get('Impact humain et urbain'),
                    photo1=row.get('Photos 1 (lien)'),
                    photo2=row.get('Photos 2 (lien)'),
                    photo3=row.get('Photos 3 (lien)'),
                    video1=row.get('Vidéos 1 (lien)'),
                    video2=row.get('Vidéos 2 (lien)'),
                    en_savoir_plus=row.get('En savoir plus (liens ressources)'),
                )
        self.stdout.write(self.style.SUCCESS('Données importées avec succès'))
