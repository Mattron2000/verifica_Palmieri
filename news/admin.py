from django.contrib import admin
from .models import articoli, giornalisti

# Register your models here.
admin.site.register(articoli)
admin.site.register(giornalisti)