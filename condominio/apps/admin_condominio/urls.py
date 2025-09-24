from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (AdminCondominioViewSet, AdminViewSet,
                    RecursoViewSet, TipoRecursoViewSet,
                    GastoViewSet, ReservaViewSet,CondominioViewSet )






router = DefaultRouter()
router.register(r'adminC', AdminViewSet, basename='adminC')
router.register(r'admin_condominio', AdminCondominioViewSet, basename='admin_condominio')
router.register(r'recurso', RecursoViewSet, basename='recurso')
router.register(r'tipo_recurso', TipoRecursoViewSet, basename='tipo_recurso')
router.register(r'gasto', GastoViewSet, basename='gasto')
router.register(r'reserva', ReservaViewSet, basename='reserva')
router.register(r'condominio', CondominioViewSet, basename='condominio')



urlpatterns = [
    
    path('', include(router.urls)),
]
