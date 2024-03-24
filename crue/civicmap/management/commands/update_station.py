import json
import requests
from datetime import datetime
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from civicmap.models import Station, Vigicrue

class Command(BaseCommand):
    help = "Mise à jour des données de hauteurs, débits et Vigicrue"

    def handle(self, *args, **kwargs):
        stations = Station.objects.all()
        for station in stations:
            # Partie débit et hauteur
            hauteur, debit, date_obs = None, None, None
            response = requests.get(
                'https://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr',
                params={'code_entite': station.code, 'size': 4}
            )
            try:
                response.raise_for_status()
                data = response.json()
                # Itérer sur les données pour extraire hauteur, débit et date
                for observation in data.get('data', []):  # Fournit une liste vide si 'data' n'est pas trouvée
                    grandeur = observation.get('grandeur_hydro')
                    resultat = observation.get('resultat_obs')
                    date_obs_str = observation.get('date_obs')
                    if grandeur == 'H':  # Hauteur
                        hauteur = resultat
                    elif grandeur == 'Q':  # Débit
                        debit = resultat
                    if date_obs_str:
                        date_obs = datetime.strptime(date_obs_str, "%Y-%m-%dT%H:%M:%SZ")
                if hauteur is not None:
                    station.hauteur = float(hauteur/1000)
                if debit is not None:
                    station.debit = float(debit/1000)
                if date_obs is not None:
                    station.date_hauteur = date_obs
                print(f"Hauteur: {hauteur}, Débit: {debit}, Date d'observation: {date_obs}")
                station.save()
            except requests.HTTPError as e:
                print(f"Erreur appel réseau: {e}")

            # Partie Vigicrue
            troncon = None
            if station.code in ("W141001001", "W141001201"):
                troncon = "AN12"
            elif station.code in ("W276721401", "W276721102"):
                troncon = "AN31"
            elif station.code=="W283201001":
                troncon = "AN30"
            url = f'https://www.vigicrues.gouv.fr/rss/?CdEntVigiCru={troncon}'
            try:
                response = requests.get(url)
                response.raise_for_status()
                try:
                    content_xml = response.text
                    root = ET.fromstring(content_xml)
                    for item in root.findall('.//item'):
                        try:
                            title = item.find('title').text
                            couleur = title.split(':')[-1].strip().lower()  # Extraire la couleur à partir du titre
                            pubDate_str = item.find('pubDate').text  # Extraire la date de publication
                            try:
                                pubDate = datetime.strptime(pubDate_str, '%a, %d %b %Y %H:%M:%S %z')
                                station.date_alerte = pubDate
                                print(f"Couleur: {couleur}, Date de publication: {pubDate}")
                                if couleur=="vert":
                                    station.niveau_alerte = Vigicrue.objects.get(niveau_alerte=1)
                                elif couleur=="jaune":
                                    station.niveau_alerte = Vigicrue.objects.get(niveau_alerte=2)
                                elif couleur=="orange":
                                    station.niveau_alerte = Vigicrue.objects.get(niveau_alerte=3)
                                elif couleur=="rouge":
                                    station.niveau_alerte = Vigicrue.objects.get(niveau_alerte=4)
                                station.save()
                            except ValueError as e:
                                print(f"Erreur lors de la conversion de la date: {e}")
                        except AttributeError as e:
                            print(f"Erreur lors de l'extraction des données d'un item: {e}")
                except ET.ParseError as e:
                    print(f"Erreur lors du parsing du XML: {e}")

            except requests.HTTPError as e:
                print(f"Erreur lors de la requête HTTP: {e}")
            except requests.RequestException as e:
                print(f"Erreur de requête: {e}")