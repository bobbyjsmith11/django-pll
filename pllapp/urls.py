from django.urls import path

from . import views
from . import pll_calcs

app_name = 'pllapp'
urlpatterns = [
        path('', views.index, name='index'),
        path('pll/', views.pll, name='pll'),
        path('solveForComponents/', pll_calcs.solveForComponents, name='solveForComponents'),
    ]
