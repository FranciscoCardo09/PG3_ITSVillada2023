from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    prestado_a = models.CharField(max_length=100)

    def __str__(self):
        return f"Prestamo de {self.libro} a {self.prestado_a}"

