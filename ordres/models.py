import uuid
from django.db import models

# Create your models here.


class Ordre(models.Model):
    """
    docstring
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    MsgId = models.CharField(max_length=100, blank=False, default='')
    creDtTm = models.DateTimeField(auto_now_add=True)
    NbOfTxs = models.IntegerField()
    ctrlSum = models.BigIntegerField()
    flwInd = models.CharField(max_length=100, blank=True, default='SIMULATOR')
    prvtDtInf = models.CharField(max_length=100, blank=True, default='CANALABBA1')
    cdOrPrtry = models.CharField(max_length=100, blank=True, default='CHANNEL')
    pmtInfId = models.CharField(max_length=100, blank=False, default='')
    pmtMtd = models.CharField(max_length=100, blank=False, default='')
    btchBookg = models.IntegerField()
    pmtInf_NbOfTxs = models.BigIntegerField()
    pmtInf_ctrlSum = models.BigIntegerField()
    ordrPrties_Tp = models.CharField(max_length=100, blank=False, default='')
    ordrPrties_Md = models.CharField(max_length=100, blank=False, default='')
    reqdExctnDt = models.DateField()
    partenaire = models.ForeignKey( 'partenaires.Partenaire', on_delete=models.CASCADE)
    pmtId_InstrId = models.CharField(max_length=100, blank=False, default='')
    pmtId_EndToEndId = models.CharField(max_length=100, blank=False, default='')
    pmtTpInf_InstrPrty = models.CharField(max_length=100, blank=False, default='')
    pmtTpInf_Prtry = models.CharField(max_length=100, blank=False, default='')
    InstdAmt = models.BigIntegerField()
    cdtr_Nm = models.CharField(max_length=100, blank=False, default='')
    cdtrAcct_id = models.BigIntegerField()
    cdtrAcct_SchmeNm = models.CharField(max_length=100, blank=False, default='')
    rmtInf = models.CharField(max_length=100, blank=False, default='')
    
    status = models.CharField( 
        max_length = 20, default = 'PAS TRAITER',
        choices = ( 
            ("PAS TRAITER", "PAS TRAITER"), 
            ("TRAITER", "TRAITER"), 
        ), 
        
    ) 
    create_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super(Ordre, self).save(*args, **kwargs)

    class Meta:
        ordering = ['create_at']