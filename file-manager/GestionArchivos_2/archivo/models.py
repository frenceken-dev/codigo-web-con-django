from django.db import models
from django.contrib.auth.models import User


TIPO_ARCHIVOS_CHOICES = [
        ('imagen', 'Imagen'),
        ('video', 'Video'),
        ('documento', 'Documento'),
        ('otros', 'Otros')
    ]

class Archivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # User se asocia con usuario.
    archivo = models.FileField(upload_to='archivos/')  # Ruta de subida para los archivos.
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_ARCHIVOS_CHOICES, default='otros')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Usuario {self.usuario.username} a subido: {self.archivo.name} de tipo {self.tipo}"   
