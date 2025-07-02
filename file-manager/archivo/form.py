from django import forms
from .models import Archivo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['archivo', 'descripcion', 'tipo']
        
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'row': 3, 'placeholder': 'Descripción de archivo'}),
            'tipo': forms.Select(attrs={'class': 'form-control'})
        }
