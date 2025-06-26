from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from .models import PasswordResetToken
from .form import CustomPasswordResetForm, CustomSetPasswordForm
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.template.loader import render_to_string
from django.urls import reverse


# Otras Vistas...
    

def custom_password_reset_request(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                token = get_random_string(length=48)
                PasswordResetToken.objects.create(user=user, token=token)
                
                reset_url = request.build_absolute_uri(reverse('ConsolaUsuarioApp:custom_password_reset_confirm', args=[token]))
                
                # constuir el contenido de la plantilla.
                context = {
                    'user':user,
                    'reset_url': reset_url,
                    'year': timezone.now().year,
                }
                html_message = render_to_string('registration/password_reset_email_custom.html', context)
                
                # Enviar Email html.
                email_message = EmailMessage(
                    subject='Restablecer Contraseña',
                    body=html_message,
                    from_email='no-responder@misitio.com',
                    to=[email]
                )
                email_message.content_subtype = 'html'
                email_message.send()
                
            except User.DoesNotExist:
                pass
            
            # uso mensaje de confirmación 
            messages.success(request, "Sí el correo existe, te hemos enviado un enlace para restablecer tu clave") # Se muestra en recuadro de inicio de sesión
            return redirect('ConsolaUsuarioApp:login')
    else:
        form = CustomPasswordResetForm()
        
    return render(request, 'registration/custom_password_reset_form.html', {'form':form})


def custom_password_reset_confirm(request, token):
    reset_token = get_object_or_404(PasswordResetToken, token=token)
    
    if not reset_token.is_valid():
        messages.error(request, 'Este enlace ha expirado, por favor solicite uno nuevo')
        return redirect('ConsolaUsuarioApp:custom_password_reset_request')
    
    if request.method == 'POST':
        form = CustomSetPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['new_password1']
            user = reset_token.user
            user.password = make_password(password)
            user.save()
            reset_token.delete()
            messages.success(request, 'Tu contraseña se ha restablecido correctamente')
            return redirect('ConsolaUsuarioApp:login')
        
    else:
        form = CustomSetPasswordForm()
            
    return render(request, 'registration/custom_password_reset_confirm.html', {'form':form})
