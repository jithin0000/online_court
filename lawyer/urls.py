from django.urls import path

from .views import lawyer_home, case_deatils


urlpatterns = [
        
        path('', lawyer_home, name='lawyer_home'),
        path('<int:pk>', case_deatils, name='lawyer_case_detail'),

        ]
