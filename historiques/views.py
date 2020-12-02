# historiques class import
from historiques.models import Historique
from historiques.serializers import HistoriqueSerializer
# user class import
#from django.contrib.auth.models import User
#from snippets.serializers import UserSerializer
# permission import
from rest_framework import permissions
#from snippets.permissions import IsOwnerOrReadOnly

from rest_framework import viewsets

from django.http import Http404
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
        #'users': reverse('user-list', request=request, format=format),
        'historiques': reverse('historique-list', request=request, format=format)
    })

# Refactoring to use ViewSets
"""
class UserViewSet(viewsets.ReadOnlyModelViewSet):
 
    This viewset automatically provides `list` and `detail` actions.
   
    queryset = User.objects.all()
    serializer_class = UserSerializer """

class HistoriqueViewSet(viewsets.ModelViewSet):
   
    queryset = Historique.objects.all()
    serializer_class = HistoriqueSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()