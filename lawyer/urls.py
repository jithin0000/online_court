from django.urls import path

from .views import lawyer_home

urlpatterns = [
        
        path('', lawyer_home, name='lawyer_home'),

        ]
