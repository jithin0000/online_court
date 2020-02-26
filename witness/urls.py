from django.urls import path

from .views import witness_home,witness_case_detail

urlpatterns = [
        path('', witness_home, name='witness_home'),
        path('<int:pk>', witness_case_detail, name='witness_case_detail'),

        ]
