from rest_framework import serializers
from django.contrib.auth.models import User
from partenaires.models import Partenaire


class PartenaireSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Partenaire
        fields = ['other_id', 'id', 'nom', 'other_schmeNm', 'brnchId_Id', 'brnchId_Nm', 'create_at']
    """
    def validate_other_schmeNm(self, value):
        qs = Partenaire.objects.filter(other_schmeNm==value)
        if qs.exists():
            raise serializers.ValidationError("Ce partenaire existe déjà")
        return value"""