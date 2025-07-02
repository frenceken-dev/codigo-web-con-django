# 🔐 Recuperación Personalizada de Contraseña con Django

Este módulo implementa un sistema completo y personalizado para recuperar la contraseña de usuarios en Django, reemplazando la solución predeterminada de `django.contrib.auth`.

---

## 🧠 Funcionalidades principales

- Formulario personalizado para solicitar el restablecimiento
- Validación del correo electrónico ingresado
- Generación de token aleatorio con expiración
- Enlace seguro construido dinámicamente
- Envío de correo HTML elegante con enlace de recuperación
- Validación del token al acceder desde el correo
- Formulario personalizado para establecer nueva contraseña
- Eliminación automática del token tras el cambio exitoso

---

## 📂 Estructura del módulo

    user-auth-reset/
    │
    ├── ConsolaUsuarioApp/
    │ ├── views.py # Vistas personalizadas
    │ ├── models.py # Modelo de token de recuperación
    │ ├── forms.py # Formularios personalizados
    │ ├── urls.py # Rutas relacionadas
    │
    ├── templates/
    │ └── registration/
    │ ├── custom_password_reset_form.html
    │ ├── custom_password_reset_confirm.html
    │ └── password_reset_email_custom.html
    │
    ├── README.md

---

## 🛠️ Tecnologías

- Python 3.10+
- Django 5.x
- Bootstrap 5 (solo para diseño de formularios)
- EmailMessage de Django para envío de correos en HTML
- Backend de consola para desarrollo

---

## 🧪 Pruebas en entorno local

En `settings.py`, debe estar configurado el backend de consola para enviar los correos al terminal:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```