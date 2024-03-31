from django.urls import path
from .views import home, slider, mobile

urlpatterns = [
    path('<int:num>/', home, name='home'),
    path('mobile/<int:num>/', mobile, name='mobile'),
    path('slider/', slider, name='slider'),
]