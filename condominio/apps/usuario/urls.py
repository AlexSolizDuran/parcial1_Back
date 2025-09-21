from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
#from .views import UsuarioViewSet

router = DefaultRouter()
#router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]
