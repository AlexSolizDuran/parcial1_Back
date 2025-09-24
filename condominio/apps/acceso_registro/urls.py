from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import NotificacionViewSet,RegistroViewSet,SeguridadViewSet,TipoVisitaViewSet,VehiculoViewSet,VisitanteViewSet

router = DefaultRouter()
router.register(r'notificacion', NotificacionViewSet, basename='notificacion')
router.register(r'registro', RegistroViewSet, basename='registro')
router.register(r'seguridad', SeguridadViewSet, basename='seguridad')
router.register(r'tipo_visita', TipoVisitaViewSet, basename='tipo_visita')
router.register(r'vehiculo', VehiculoViewSet, basename='vehiculo')
router.register(r'visitante', VisitanteViewSet, basename='visitante')

urlpatterns = [
    
    path('', include(router.urls)),
]
