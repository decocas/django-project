 
from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #identificacion = models.ForeingKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    #text = models.TextField()
    fecha = models.DateTimeField(
            default=timezone.now)
    publicacion = models.DateTimeField(
            blank=True, null=True)

    def publicar(self):
        self.publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
