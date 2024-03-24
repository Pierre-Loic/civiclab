from django.shortcuts import render
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from .models import Station, Vigicrue, RepereCrue

def carte(request):
    reperes = serialize('json', RepereCrue.objects.all(), fields=('id_gsheet', 'latitude', 'longitude'))
    print(reperes)
    stations = Station.objects.all() 

    stations = serialize('json', Station.objects.all())
    data = Vigicrue.objects.get(niveau_alerte=1)
    data_dict = model_to_dict(data)
    return render(request, 'civicmap/carte.html', {'stations': stations, 'data': data_dict, 'reperes': reperes})

def carte_mobile(request):
    reperes = serialize('json', RepereCrue.objects.all(), fields=('id_gsheet', 'latitude', 'longitude'))
    print(reperes)
    stations = Station.objects.all() 

    stations = serialize('json', Station.objects.all())
    data = Vigicrue.objects.get(niveau_alerte=1)
    data_dict = model_to_dict(data)
    return render(request, 'civicmap/carte_mobile.html', {'stations': stations, 'data': data_dict, 'reperes': reperes})