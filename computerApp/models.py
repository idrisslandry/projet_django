
from django.db import models
from django.urls import reverse


class Commu(models.Model): #Class de base
    name= models.CharField(max_length= 19)
    slug = models.SlugField(max_length=128)
    marque = models.CharField(max_length= 128)
    administrateur = models.CharField(max_length= 20)
    zone = models.CharField(max_length= 50)
    configuration = models.TextField(blank=True)
    detail = models.TextField(blank=True) 
    thumbnail = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__ (self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("commu_detail", kwargs={"slug": self.slug})
   


class Routeur(models.Model):
    name = models.CharField(max_length= 19)
    slug = models.SlugField(max_length=128)
    marque = models.CharField(max_length= 128)
    administrateur = models.CharField(max_length= 20)
    zone = models.CharField(max_length= 50)
    configuration = models.TextField(blank=True)
    detail = models.TextField(blank=True) #Pas forcement de description
    thumbnail = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__ (self):
        return str(self.name)
        
    def get_absolute_url(self):
        return reverse("routeur_detail", kwargs={"slug": self.slug})