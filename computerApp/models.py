import datetime
from django.db import models

# Create your models here.
class Machine(models.Model):
    TYPE = (
        ('PC',('PC - Run windows')),
        ('Mac',('MAc - Run MacOS')),
        ('Serveur',('Serveur - Simple Server to deploy virtual machines')),
        ('Switch',('Switch - To maintains and connect servers')),
    )
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    nom= models.CharField(
                max_length=6)
    maintenaceDate = models.DateField(default= datetime.datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE,default='PC')
    def __str__(self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom
    
class Personnel(models.Model):
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    nom= models.CharField(
                max_length=10)
    prenom= models.CharField(
                max_length=10,
                default="")
    def __str__(self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

    def get_surname(self):
        return str(self.id) + " " + self.prenom