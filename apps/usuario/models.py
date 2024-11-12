from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.CharField(max_length=20, null=False)
    telefono = models.CharField(max_length=20)

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

class Agente(Usuario):
    matricula = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.matricula}'

    class Meta:
        verbose_name = "Agente"
        verbose_name_plural = "Agentes"

class Cliente(Usuario):
    pass

    def __str__(self):
        return f'{self.first_name} {self.last_name} - Cliente ({self.dni})'

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Moderador(Usuario):
    pass

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Moderador"
        verbose_name_plural = "Moderadores"
