from .models import articoli, giornalisti
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import articoli, giornalisti
from django.shortcuts import get_list_or_404, get_object_or_404

def home(request):
    return render(request, "home.html")

class listaArticoli(ListView):
    model = articoli #modello dei dati da utilizzare 
    template_name = "news/articoli.html"  #pagina per mostrare i dati

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"] = articoli.objects.all()
        return context

class listaGiornalisti(ListView):
    model = giornalisti #modello dei dati da utilizzare 
    template_name = "news/giornalisti.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["giornalisti"] = giornalisti.objects.all()
        return context