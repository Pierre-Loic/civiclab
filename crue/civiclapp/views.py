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
    if data_repere["presentation_crue"]=="":
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
    return render(request, 'civiclapp/home.html', {"type" : "desktop", "data" : data_dict, "data_repere" : data_repere, "slides" : slides, "station" : station})

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
    if data_repere["presentation_crue"]=="":
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
    return render(request, 'civiclapp/home.html', {"type" : "mobile", "data" : data_dict, "data_repere" : data_repere, "slides" : slides, "station" : station})

@xframe_options_exempt
def slider(request):
    return render(request, 'civiclapp/slider.html')
