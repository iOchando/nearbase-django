from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('domain', views.DomainViewSet)
router.register('domain-credentials', views.DomainCredentialsViewSet)
router.register('market', views.MarketViewSet)
router.register('profile', views.ProfileViewSet)
#router.register('profilelibrary', views.ProfileLibraryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('node-token', views.node_token),
    
]