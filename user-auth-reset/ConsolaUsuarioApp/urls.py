from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

app_name = 'ConsolaUsuarioApp'  # Agrega esto para definir el espacio de nombres

urlpatterns = [
    # Otras Urls...    
    path('password_reset/', views.custom_password_reset_request, name='custom_password_reset'),
    path('password_reset/confirm/<str:token>/', views.custom_password_reset_confirm, name='custom_password_reset_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)