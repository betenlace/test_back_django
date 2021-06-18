from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField("Nombre",max_length=255)
    doc = models.CharField("Identificacion",max_length=255)
    profile =  models.CharField("Perfil", max_length=255)
    class Meta:
        verbose_name="User"
        verbose_name_plural="Users"

    def __str__(self):
        return f"{self.id} - {self.name}"