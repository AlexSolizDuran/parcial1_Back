# utils.py
import cv2
import numpy as np
import json
from .models import Persona

def generar_vector_facial_opencv(persona):
    """
    Genera un vector facial usando OpenCV y lo guarda en persona.face_vector
    """
    if not persona.foto:
        return False  # No hay foto

    try:
        # 1. Leer imagen desde la ruta del modelo
        img = cv2.imread(persona.foto.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 2. Detectar la cara
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) == 0:
            return False  # No se detectó cara

        # 3. Tomar la primera cara detectada
        x, y, w, h = faces[0]
        face_img = gray[y:y+h, x:x+w]

        # 4. Normalizar tamaño
        face_img = cv2.resize(face_img, (100, 100))

        # 5. Convertir a vector 1D
        face_vector = face_img.flatten()

        # 6. Guardar en JSON en la base de datos
        persona.face_vector = json.dumps(face_vector.tolist())
        persona.save()

        return True

    except Exception as e:
        print(f"Error generando vector facial: {e}")
        return False
