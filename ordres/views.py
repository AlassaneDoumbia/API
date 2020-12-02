from django.shortcuts import render

# snippets class import
from ordres.models import Ordre
from ordres.serializers import OrdreSerializer
# permission import
from rest_framework import permissions

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
        'ordres': reverse('ordre-list', request=request, format=format)
    })


class OrdreViewSet(viewsets.ModelViewSet):
    
    queryset = Ordre.objects.all()
    serializer_class = OrdreSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        #serializer.save(owner=self.request.user)
        serializer.save()