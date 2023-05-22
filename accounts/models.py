from django.contrib.auth.models import AbstractUser
from django.db import models

from computermngt.settings import AUTH_USER_MODEL

class User(AbstractUser): # utilisateur avec un login et un mp
    pass


    

class Compte(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    connexion_date = models.DateTimeField(blank=True, null=True)
    def __str_(self):
        return self.user.username

    