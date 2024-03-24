from django.urls import path
from .views import carte, carte_mobile

urlpatterns = [
    path('', carte, name='carte'),
    path('mobile/', carte_mobile, name='carte_mobile'),
]