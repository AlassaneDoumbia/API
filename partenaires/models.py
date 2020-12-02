import uuid
from django.db import models

# Create your models here.


class Partenaire(models.Model):
    """
    docstring
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100, blank=False, default='')
    other_id = models.CharField(max_length=100, blank=False, default='')
    other_schmeNm = models.CharField(max_length=100, blank=False, default='')
    brnchId_Id = models.CharField(max_length=100, blank=False, default='')
    brnchId_Nm = models.CharField(max_length=100, blank=False, default='')
    create_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super(Partenaire, self).save(*args, **kwargs)

    class Meta:
        ordering = ['create_at']