from rest_framework.urlpatterns import format_suffix_patterns
#from snippets.views import SnippetViewSet, UserViewSet, api_root
from historiques.views import HistoriqueViewSet, api_root
from partenaires.views import PartenaireViewSet
from suivis.views import SuiviViewSet
from ordres.views import OrdreViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'historiques', HistoriqueViewSet)
router.register(r'suivis', SuiviViewSet)
router.register(r'ordres', OrdreViewSet)
router.register(r'partenaires', PartenaireViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]