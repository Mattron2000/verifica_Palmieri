from django.db import models

# Create your models here.
class articoli(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    autore = models.ForeignKey('giornalisti', on_delete=models.CASCADE, related_name="giornalista", default=1)
    #data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo

class giornalisti(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    #data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome + " " + self.cognome