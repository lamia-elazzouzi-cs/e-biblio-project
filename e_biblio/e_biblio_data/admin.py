from django.contrib import admin
from .models import Ouvrage, Chercheur, Emprunt
# Register your models here.

admin.site.register(Ouvrage)
admin.site.register(Chercheur)
admin.site.register(Emprunt)
