from django import forms

class EquipoForm(forms.Form):
    nombre = forms.CharField(max_length=20)

class FifaForm(forms.Form):
    nom = forms.CharField(max_length=30)
    club = forms.CharField(max_length=30)