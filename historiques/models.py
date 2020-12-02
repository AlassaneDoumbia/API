import uuid
from django.db import models

# Create your models here.


class Historique(models.Model):
    """
    docstring
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    libelle = models.CharField(max_length=100, blank=False )
    nom_document = models.CharField(max_length=100, blank=True, default='')
    montant_paye = models.BigIntegerField(default=False)
    nbre_virement_effectif = models.BigIntegerField(default=False)
    nbre_virement_non_effectif = models.BigIntegerField(default=False)
    date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super(Historique, self).save(*args, **kwargs)

    class Meta:
        ordering = ['date']