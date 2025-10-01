from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserViewSet, PersonaViewSet,RolViewSet,RolUsuarioViewSet,FacialView



router = DefaultRouter()
router.register(r'usuarios', UserViewSet, basename='usuario')
router.register(r'personas',PersonaViewSet,basename='persona')
router.register(r'roles',RolViewSet,basename='rol')
router.register(r'rol_usuario',RolUsuarioViewSet,basename='rol_usuario')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('facial/', FacialView.as_view(), name='facial'),
]
