from django.urls import path

from . import views

app_name = 'ContractMaker'

urlpatterns = [
    path('', views.index, name='index')
]
