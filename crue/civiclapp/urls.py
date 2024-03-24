from django.urls import path
from .views import home, slider, fictif, bootstrap, mobile

urlpatterns = [
    path('<int:num>/', home, name='home'),
    path('fictif/<int:num>/', fictif, name='fictif'),
    path('bootstrap/<int:num>/', bootstrap, name='bootstrap'),
    path('mobile/<int:num>/', mobile, name='mobile'),
    path('slider/', slider, name='slider'),
]