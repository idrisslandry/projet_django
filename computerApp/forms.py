
from django.forms import ModelForm


from computerApp.models import Commu, Routeur
#from django.views.generic import DeleteView, UpdateView


class Add_commu_form(ModelForm):
    class Meta: #class qui utilise une classe
        model = Commu # Quel modele utilisé pour créer le formulaire
        fields = ['name', 'slug', 'marque', 'administrateur', 'zone', 'configuration', 'detail', 'thumbnail'] #Les champs a afficher


class Add_routeur_form(ModelForm):
    class Meta: #class qui utilise une classe
        model = Routeur # Quel modele utilisé pour créer le formulaire
        fields = ['name', 'slug', 'marque', 'administrateur', 'zone', 'configuration', 'detail', 'thumbnail'] #Les champs a afficher




class Edit_commu_form(ModelForm):
  class Meta: #class qui utilise une classe
      model = Commu # Quel modele utilisé pour créer le formulaire
      fields = ['name', 'slug', 'marque', 'administrateur', 'zone', 'configuration', 'detail', 'thumbnail'] #Les champs a afficher


class Edit_routeur_form(ModelForm):
    class Meta: #class qui utilise une classe
      model = Routeur # Quel modele utilisé pour créer le formulaire
      fields = ['name', 'slug', 'marque', 'administrateur', 'zone', 'configuration', 'detail', 'thumbnail'] #Les champs a afficher

