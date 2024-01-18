from django.urls import path
from .import views

urlpatterns = [
    path('', views.spr05, name='')
]
