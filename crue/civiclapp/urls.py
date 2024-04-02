from django.urls import path
from .views import home, slider, mobile, slider_2

urlpatterns = [
    path('<int:num>/', home, name='home'),
    path('mobile/<int:num>/', mobile, name='mobile'),
    path('slider/', slider, name='slider'),
    path('slider-2/', slider_2, name='slider-2'),
]