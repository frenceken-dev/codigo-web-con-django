from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_archivos, name='lista_archivos'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='archivo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='archivo/logout.html', next_page='login'), name='logout_usuario'),
    path('subir/', views.subir_archivo, name='subir_archivo'),
    path('eliminar/<int:id_archivo>/', views.eliminar_archivo, name='eliminar_archivo'),
]
