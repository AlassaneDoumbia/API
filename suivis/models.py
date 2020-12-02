import uuid
from django.db import models

# Create your models here.


class Suivi(models.Model):
    """
    docstring
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    libelle = models.CharField(max_length=100, blank=False, default='')
    ordre = models.ForeignKey( 'ordres.Ordre', on_delete=models.CASCADE)
    status = models.CharField( 
        max_length = 20, default = 'EN COURS',
        choices = ( 
            ("EN COURS", "EN COURS"), 
            ("BLOQUÉ", "BLOQUÉ"), 
            ("FINI", "FINI"), 
        ), 
        
    ) 
    create_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super(Suivi, self).save(*args, **kwargs)

    class Meta:
        ordering = ['create_at']