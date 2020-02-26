from django.urls import path

from .views import user_home, user_case_detail

urlpatterns = [
        path('', user_home, name='user_home'),
        path('<int:pk>', user_case_detail, name='user_case_detail'),
        ]

