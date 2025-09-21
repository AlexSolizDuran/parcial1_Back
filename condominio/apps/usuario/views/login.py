from rest_framework import generics, permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status                                                                                                                                                                                                                                                                                                                               

class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        if user is not None:
            
            
            refresh = RefreshToken.for_user(user)
    # Agregar información extra al payload del access token
            refresh['username'] = user.username
            roles = list(user.roles.values_list('nombre', flat=True))
            refresh['roles'] = roles
            
            
            response = Response({
            'access_token': str(refresh.access_token),
            'roles': roles
            },status = status.HTTP_200_OK)
        
            response.set_cookie(
                key="refreshToken",
                value=refresh,
                httponly=True,
                secure=False,
                samesite="Strict",
            )
            return response
        
        return Response({'details': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        response = Response({'details','Logout exitoso'},status=status.HTTP_200_OK)
        response.delete_cookie('refreshToken')
        return response
          
