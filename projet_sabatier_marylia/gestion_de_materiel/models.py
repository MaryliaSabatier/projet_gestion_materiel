from django.db import models
from django.urls import reverse

class Enseignant(models.Model):
    nom = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default='aucun'
    )
    prenom = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default='aucun'
    )

class Salle(models.Model):
    nom = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default='aucun'
    )
    etage = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        default='aucun'
    )


class Materiel(models.Model):
    nom = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default=''
    )
    budget = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default=''
    )
    proprietaire = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        related_name='materiels_possedes'
    )
    lieu = models.ForeignKey(
        Salle,
        on_delete=models.CASCADE,
        null=True
    )
    possesseur = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='materiels_en_possession'
    )

class TransfertMateriel(models.Model):
    material = models.ForeignKey(
        Materiel,
        on_delete=models.CASCADE,
        null=True
    )
    ancien_possesseur = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        related_name='transferts_sortants'
    )
    nouveau_possesseur = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        related_name='transferts_entrants'
    )
    date_transfert = models.DateField()
    ancien_lieu = models.ForeignKey(
        Salle,
        on_delete=models.CASCADE,
        related_name='transferts_sortants',
        null=True
    )
    nouveau_lieu = models.ForeignKey(
        Salle,
        on_delete=models.CASCADE,
        related_name='transferts_entrants',
        null=True
    )
    occasion = models.CharField(
        max_length=100
    )
    objectif = models.TextField()

class AccessoireMateriel(models.Model):
    material = models.ForeignKey(
        Materiel,
        on_delete=models.CASCADE,
        null=True
    )
    nom = models.CharField(
        max_length=100,
        blank = True
    )
    present = models.BooleanField(
        default=True
    )
    etat = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

class TransfertAccessoire(models.Model):
    transfert = models.ForeignKey(
        TransfertMateriel,
        on_delete=models.CASCADE
    )
    accessoire = models.ForeignKey(
        AccessoireMateriel,
        on_delete=models.CASCADE
    )
    ancienne_presence = models.BooleanField(
        default=True
    )
    nouvelle_presence = models.BooleanField(
        default=True
    )
    ancien_etat = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    nouveau_etat = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
