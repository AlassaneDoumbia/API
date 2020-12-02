from rest_framework import serializers
from suivis.models import Suivi
from ordres.serializers import OrdreSerializer


class SuiviSerializer(serializers.HyperlinkedModelSerializer):
    
    ordre = OrdreSerializer(many=True, read_only=True)
    class Meta:
        model = Suivi
        fields = ['libelle', 'id', 'ordre', 'status', 'create_at']
