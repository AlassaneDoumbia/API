
from historiques.views import HistoriqueViewSet, api_root
from rest_framework import renderers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from historiques import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'historiques', HistoriqueViewSet)
#router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]