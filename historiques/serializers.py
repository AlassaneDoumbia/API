from rest_framework import serializers
from django.contrib.auth.models import User
from historiques.models import Historique


class HistoriqueSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Historique
        fields = ['montant_paye', 'id', 'nom_document',# 'owner',
                  'libelle', 'nbre_virement_effectif', 'nbre_virement_non_effectif', 'date']

    def validate_montant_paye(self, value):
        if value < 0:
            raise serializers.ValidationError("La valeur ne doit pas être négatif")
        return value

    def validate_nbre_virement_effectif(self, value):
        if value < 0:
            raise serializers.ValidationError("La valeur ne doit pas être négatif")
        return value

    def validate_nbre_virement_non_effectif(self, value):
        if value < 0:
            raise serializers.ValidationError("La valeur ne doit pas être négatif")
        return value
"""
    def validate_nbre_virement_non_effectif(self, value):
        qs = Historique.objects.filter(id=value)
        if qs.exists():
            return value
        raise serializers.ValidationError("Merci de donner une clé correct")"""