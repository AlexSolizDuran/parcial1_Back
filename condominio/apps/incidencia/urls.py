from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MultaViewSet,FotoViewSet,ReclamoViewSet,TipoMultaViewSet 


router = DefaultRouter()
router.register(r'multa', MultaViewSet, basename='multa')
router.register(r'foto', FotoViewSet, basename='foto')
router.register(r'reclamo', ReclamoViewSet, basename='reclamo')
router.register(r'tipo_multa', TipoMultaViewSet, basename='tipo_multa')


urlpatterns = [
    path('', include(router.urls)),
]
