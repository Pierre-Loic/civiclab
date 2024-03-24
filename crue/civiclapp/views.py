from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.forms.models import model_to_dict
from civicmap.models import Vigicrue, RepereCrue

def home(request, num):
    if num is not None:
        # Récupération du repère de crue dans la BDD
        repere = RepereCrue.objects.get(id_gsheet=num)
        data_repere = model_to_dict(repere)
        # Récupération des données de la station

        # Récupération des données Vigicrue
        data = repere.code_station.niveau_alerte
        data_dict = model_to_dict(data)
    else:
        data = Vigicrue.objects.get(niveau_alerte=1)
        data_dict = model_to_dict(data)
    return render(request, 'civiclapp/home.html', {"data" : data_dict, "data_repere" : data_repere})


def fictif(request, num):
    if num is not None:
        # Récupération du repère de crue dans la BDD
        repere = RepereCrue.objects.get(id_gsheet=num)
        data_repere = model_to_dict(repere)
        # Récupération des données de la station

        # Récupération des données Vigicrue
        data = repere.code_station.niveau_alerte
        data_dict = model_to_dict(data)
    else:
        data = Vigicrue.objects.get(niveau_alerte=1)
        data_dict = model_to_dict(data)
    return render(request, 'civiclapp/home_responsive.html', {"data" : data_dict, "data_repere" : data_repere})

@xframe_options_exempt
def bootstrap(request, num):
    if num is not None:
        # Récupération du repère de crue dans la BDD
        repere = RepereCrue.objects.get(id_gsheet=num)
        data_repere = model_to_dict(repere)
        # Récupération des données de la station

        # Récupération des données Vigicrue
        data = repere.code_station.niveau_alerte
        data_dict = model_to_dict(data)
    else:
        data = Vigicrue.objects.get(niveau_alerte=1)
        data_dict = model_to_dict(data)
    # Envoi des noms des templates du slider
    slides = [
        "civiclapp/slide_2.html",
        "civiclapp/slide_3.html",
        "civiclapp/slide_4.html",
    ]
    return render(request, 'civiclapp/home_bootstrap.html', {"data" : data_dict, "data_repere" : data_repere, "slides" : slides})

def mobile(request, num):
    if num is not None:
        # Récupération du repère de crue dans la BDD
        repere = RepereCrue.objects.get(id_gsheet=num)
        data_repere = model_to_dict(repere)
        # Récupération des données de la station

        # Récupération des données Vigicrue
        data = repere.code_station.niveau_alerte
        data_dict = model_to_dict(data)
    else:
        data = Vigicrue.objects.get(niveau_alerte=1)
        data_dict = model_to_dict(data)
    # Envoi des noms des templates du slider
    slides = [
        "civiclapp/slide_1.html",
        "civiclapp/slide_2.html",
        "civiclapp/slide_3.html",
        "civiclapp/slide_4.html",
        "civiclapp/slide_5.html",
    ]
    return render(request, 'civiclapp/home_bootstrap.html', {"data" : data_dict, "data_repere" : data_repere, "slides" : slides})

@xframe_options_exempt
def slider(request):
    return render(request, 'civiclapp/slider.html')
