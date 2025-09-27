from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MascotaViewSet,
    InquilinoViewSet,
    ContratoViewSet,
    HistorialDueñoViewSet,
    ViviendaViewSet,
    NumeroParqueoViewSet,
    ParqueoViewSet,
    PropietarioViewSet,
    OcupanteViewSet,
    PropietarioViviendaViewSet
    
)
router = DefaultRouter()
router.register(r'mascota', MascotaViewSet, basename='mascota')
router.register(r'inquilino', InquilinoViewSet, basename='inquilino')
router.register(r'contrato', ContratoViewSet, basename='contrato')
router.register(r'historial_dueño', HistorialDueñoViewSet, basename='historial_dueño')
router.register(r'vivienda', ViviendaViewSet, basename='vivienda')
router.register(r'numero_parqueo', NumeroParqueoViewSet, basename='numero_parqueo')
router.register(r'parqueos', ParqueoViewSet, basename='parqueos')
router.register(r'propietario', PropietarioViewSet, basename='propietario') 
router.register(r'ocupante', OcupanteViewSet, basename='ocupante')
router.register(r'propietario_vivienda', PropietarioViviendaViewSet, basename='propietario_vivienda')


urlpatterns = [
    path('', include(router.urls)),
]
