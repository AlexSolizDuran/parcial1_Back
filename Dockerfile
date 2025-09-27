FROM python:3.11
# Configuración Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2 y compilación
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias e instalarlas
COPY requirementx.txt .
RUN pip install --no-cache-dir -r requirementx.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto
EXPOSE 8080

# Comando para arrancar Django con Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8080", "condominio.wsgi:application"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]