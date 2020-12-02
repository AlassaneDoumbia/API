# suivis class import
from suivis.models import Suivi
from suivis.serializers import SuiviSerializer
# permission import
from rest_framework import permissions
#from snippets.permissions import IsOwnerOrReadOnly

from rest_framework import viewsets
#import rest framework
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

#create a  single entry point 
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'suivis': reverse('suivi-list', request=request, format=format)
    })


class SuiviViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Suivi.objects.all()
    serializer_class = SuiviSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()