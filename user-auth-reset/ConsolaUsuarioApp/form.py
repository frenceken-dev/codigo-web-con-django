from django import forms
from .models import Suscripcion
        

# Otros formularios...


class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(
        label="correo electrónico", max_length=300, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control login-container',
            'placeholder': 'Escribe tu correo aquí',
            'type': 'email',
            'required': True
        })
    )
    

class CustomSetPasswordForm(forms.Form):
    new_password1 = forms.CharField(
        label='Nueva Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nueva Contraseña'
        }), strip=False
    )
    
    new_password2 = forms.CharField(
        label='Confirmar Nueva Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar Nueva Contraseña'
        }), strip=False
    )
    
    def clean(self):
        cleaned_data = super().clean()
        P1 = cleaned_data.get('new_password1')
        P2 = cleaned_data.get('new_password2')
        if P1 and P2 and P1 != P2:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cleaned_data