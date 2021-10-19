from django.db import models


# Create your models here.
class Chercheur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "%s - %s" % (self.nom, self.email)


class Ouvrage(models.Model):
    titre = models.CharField(max_length=200)
    auteurs = models.CharField(max_length=100)
    editeur = models.CharField(max_length=100)
    date_publication = models.CharField(max_length=100)
    examplaires_dispo = models.IntegerField()
    specialite = models.CharField(max_length=200)

    def __str__(self):
        return "%s (%s %s, %s) %s livres disponibles - spécialité = %s" % (self.titre,self.auteurs,self.date_publication,self.editeur,self.examplaires_dispo,self.specialite)


class Emprunt(models.Model):
    id_chercheur = models.ForeignKey(Chercheur, on_delete=models.CASCADE)
    id_ouvrage = models.ForeignKey(Ouvrage, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (%s)" % (self.id_ouvrage,self.id_chercheur)


"""
    Structure de la base de données:
        * ouvrage:
        -id
        -titre
        -auteurs
        -editeur
        -date publication
        -nbr exemplaires
        -la spécialité
        
        * Chercheur:
        -id
        -name
        -email
        
        * emprunts/librairie (or ouvragesChercheur):
        -id
        -foreign key de l'ouvrage
        -nom chercheur
"""
