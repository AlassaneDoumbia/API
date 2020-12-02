from rest_framework import serializers
from django.contrib.auth.models import User
from ordres.models import Ordre
from partenaires.serializers import PartenaireSerializer


class OrdreSerializer(serializers.HyperlinkedModelSerializer):
    partenaire = PartenaireSerializer(many=True, read_only=True)

    class Meta:
        model = Ordre
        fields = ['MsgId', 'id', 'NbOfTxs', 'creDtTm', 'ctrlSum', 'flwInd', 'prvtDtInf',  'cdOrPrtry', 'pmtInfId', 
                'pmtMtd' ,'btchBookg', 'pmtInf_NbOfTxs','pmtInf_ctrlSum', 'ordrPrties_Tp', 'ordrPrties_Md', 
                'partenaire', 'pmtId_InstrId', 'pmtId_EndToEndId', 'pmtTpInf_InstrPrty', 'pmtTpInf_Prtry', 
                'InstdAmt', 'cdtr_Nm', 'cdtrAcct_id', 'cdtrAcct_SchmeNm', 'rmtInf', 'status', 'create_at']
