from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (DetalleFacturaViewSet, FacturaViewSet,
                    ExpensaViewSet,ExpensaViviendaViewSet,
                    TipoPagoViewSet,NotaAlquilerViewSet,
                    ServicioBasicoViewSet,PagoViewSet,TipoExpensaViewSet)
router = DefaultRouter()
router.register(r'detalle_factura', DetalleFacturaViewSet, basename='detalle_factura')
router.register(r'factura', FacturaViewSet , basename='factura')
router.register(r'expensa', ExpensaViewSet, basename='expensa')
router.register(r'expensa_vivienda', ExpensaViviendaViewSet, basename='expensa_vivienda')
router.register(r'tipo_pago', TipoPagoViewSet, basename='tipo_pago')
router.register(r'nota_alquiler', NotaAlquilerViewSet, basename='nota_alquiler')
router.register(r'servicio_basico', ServicioBasicoViewSet, basename='servicio_basico')
router.register(r'pago', PagoViewSet, basename='pago')
router.register(r'tipo_expensa', TipoExpensaViewSet, basename='tipo_expensa')




urlpatterns = [
    path('', include(router.urls)),
]
