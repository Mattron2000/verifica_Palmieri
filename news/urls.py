from django.urls import path
from . import views
from .views import listaArticoli, listaGiornalisti, listArtGiorn

app_name = 'news'
urlpatterns = [
    path('', views.home, name='home'),
    path('articoli', listaArticoli.as_view(), name='lista-articoli'),
    path('articoli/<int:pk>', listArtGiorn, name='lista-articoli-giornalisti'),
    path('giornalisti', listaGiornalisti.as_view(), name='lista-giornalisti'),
]