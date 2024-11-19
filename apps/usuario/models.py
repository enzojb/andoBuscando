from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.CharField(max_length=20, null=False)
    telefono = models.CharField(max_length=20)
    
    is_agente = models.BooleanField(default=False)
    matricula = models.CharField(max_length=20, null=True, blank=True)
    is_moderador = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"