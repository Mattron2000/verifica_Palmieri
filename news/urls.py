from django.urls import path
from . import views
from .views import listaArticoli, listaGiornalisti

app_name = 'news'
urlpatterns = [
    path('', views.home, name='home'),
    path('articoli', listaArticoli.as_view(), name='lista-articoli'),
    path('giornalisti', listaGiornalisti.as_view(), name='lista-giornalisti'),
]