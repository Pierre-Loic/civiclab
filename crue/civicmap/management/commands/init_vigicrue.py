import json
from django.core.management.base import BaseCommand
from civicmap.models import Vigicrue

class Command(BaseCommand):
    help = "Charge les données Vigicrue d'initialisation à partir d'un fichier JSON"

    def handle(self, *args, **kwargs):
        # Étape 1: Suppression des données existantes
        Vigicrue.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Données existantes supprimées avec succès'))

        # Étape 2: Insertion des données
        with open('data/init_vigicrue.json', 'r', encoding='utf-8') as json_file:
            vigicrue_data = json.load(json_file)
            for index, entry in enumerate(vigicrue_data):
                Vigicrue.objects.create(
                    niveau_alerte=int(entry['niveau_alerte']),
                    time=entry['time'],
                    main_color=entry['main_color'],
                    color_4=entry['color_4'],
                    color_3=entry['color_3'],
                    color_2=entry['color_2'],
                    color_1=entry['color_1'],
                    text=entry['text'],
                    full_text=entry['full_text'],
                )
            self.stdout.write(self.style.SUCCESS('Les données Vigicrue ont été chargées avec succès !'))
