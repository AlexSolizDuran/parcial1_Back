# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import FacialSerializer
from rest_framework import permissions
from ..models import Persona
import cv2
import numpy as np
import json

class FacialView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = FacialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image_file = serializer.validated_data['image']

        # Decodificar la imagen enviada desde Flutter o frontend
        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Convertir a gris y detectar la cara
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) == 0:
            return Response({"detail": "No se detectó ninguna cara"}, status=status.HTTP_400_BAD_REQUEST)

        # Tomamos la primera cara detectada
        x, y, w, h = faces[0]
        face_img = gray[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (100, 100))  # Normalizamos tamaño
        face_vector = face_img.flatten()

        # Comparar con vectores guardados en la DB
        personas = Persona.objects.exclude(face_vector__isnull=True)
        threshold = 0.6  # Ajustar según prueba
        encontrado = None

        for p in personas:
            db_vector = np.array(json.loads(p.face_vector))
            min_len = min(len(db_vector), len(face_vector))
            dist = np.linalg.norm(db_vector[:min_len] - face_vector[:min_len])
            if dist < threshold:
                encontrado = p
                break

        if encontrado:
            return Response({
                "detail": "Persona reconocida",
                "id": encontrado.id,
                "nombre": encontrado.nombre,
                "apellido": encontrado.apellido
            })

        return Response({"detail": "No se encontró coincidencia"}, status=status.HTTP_404_NOT_FOUND)
