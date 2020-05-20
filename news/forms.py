from django import forms
from .models import articoli, giornalisti


'''class ArticoloForm(forms.ModelForm):
    class Meta:
        model = articoli
        #fields = "__all__"
        fields = ["titolo","contenuto"]

class GiornalistaForm(forms.ModelForm):
    class Meta:
        model = giornalisti
        #fields = "__all__"
        fields = ["nome","cognome"]'''