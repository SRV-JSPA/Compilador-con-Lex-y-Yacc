# Usa una imagen oficial de Python
FROM python:3.12

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instala las dependencias necesarias
RUN pip install ply

# Ejecuta el programa
CMD ["python", "parser.py"]
