from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AdminCondominioViewSet, AdminViewSet, RecursoViewSet, TipoRecursoViewSet, GastoViewSet, ReservaViewSet






router = DefaultRouter()
router.register(r'adminC', AdminViewSet, basename='adminC')
router.register(r'admin_condominio', AdminCondominioViewSet, basename='admin_condominio')
router.register(r'recurso', RecursoViewSet, basename='recurso')
router.register(r'tipo_recurso', TipoRecursoViewSet, basename='tipo_recurso')
router.register(r'gasto', GastoViewSet, basename='gasto')
router.register(r'reserva', ReservaViewSet, basename='reserva')


urlpatterns = [
    
    path('', include(router.urls)),
]
