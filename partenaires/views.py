# partenaires class import
from partenaires.models import Partenaire
from partenaires.serializers import PartenaireSerializer
# permission import
from rest_framework import permissions
#from snippets.permissions import IsOwnerOrReadOnly

from rest_framework import viewsets

#import rest framework
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

#create a  single entry point 
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'partenaires': reverse('partenaire-list', request=request, format=format)
    })


class PartenaireViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()