from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.forms.models import model_to_dict
from civicmap.models import Vigicrue, RepereCrue

@xframe_options_exempt
def home(request, num):
    if num is not None:
        # Récupération du repère de crue dans la BDD
        repere = RepereCrue.objects.get(id_gsheet=num)
        data_repere = model_to_dict(repere)
        # Récupération des données de la station
        station = model_to_dict(repere.code_station)
        # Récupération des données Vigicrue
        data = repere.code_station.niveau_alerte
        data_dict = model_to_dict(data)
    else:
        data = Vigicrue.objects.get(niveau_alerte=1)
        data_dict = model_to_dict(data)
    # Envoi des noms des templates du slider
    if data_repere["photo1"]=="":
        slides = [
            "civiclapp/slide_2.html",
            "civiclapp/slide_3.html",
        ]
    else:
        slides = [
        "civiclapp/slide_2.html",
        "civiclapp/slide_3.html",
        "civiclapp/slide_4.html",
        ]
    hauteur = int(555 - 555 * (float(station["hauteur"])+1) / 5.5)
    return render(request, 'civiclapp/home.html', {"type" : "desktop", "data" : data_dict, "data_repere" : data_repere, "slides" : slides, "station" : station, "hauteur" : hauteur})

def mobile(request, num):
    if num is not None:
        # Récupération du repère de crue dans la BDD
        repere = RepereCrue.objects.get(id_gsheet=num)
        data_repere = model_to_dict(repere)
        # Récupération des données de la station
        station = model_to_dict(repere.code_station)
        # Récupération des données Vigicrue
        data = repere.code_station.niveau_alerte
        data_dict = model_to_dict(data)
    else:
        data = Vigicrue.objects.get(niveau_alerte=1)
        data_dict = model_to_dict(data)
    # Envoi des noms des templates du slider
    if data_repere["photo1"]=="":
        slides = [
            "civiclapp/slide_1.html",
            "civiclapp/slide_2.html",
            "civiclapp/slide_3.html",
            "civiclapp/slide_5.html",
        ]
    else:
        slides = [
            "civiclapp/slide_1.html",
            "civiclapp/slide_2.html",
            "civiclapp/slide_3.html",
            "civiclapp/slide_4.html",
            "civiclapp/slide_5.html",
        ]
    hauteur = int(555 - 555 * (float(station["hauteur"])+1) / 5.5)
    return render(request, 'civiclapp/home.html', {"type" : "mobile", "data" : data_dict, "data_repere" : data_repere, "slides" : slides, "station" : station, "hauteur" : hauteur})

@xframe_options_exempt
def slider(request):
    return render(request, 'civiclapp/slider.html')

@xframe_options_exempt
def slider_2(request):
    return render(request, 'civiclapp/slider_2.html')
