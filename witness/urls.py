from django.urls import path

from .views import witness_home

urlpatterns = [
        path('', witness_home, name='witness_home'),

        ]
