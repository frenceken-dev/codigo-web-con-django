from django.shortcuts import render, redirect, get_object_or_404
from .form import ArchivoForm
from .models import Archivo
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseForbidden


@login_required(login_url='login')
def lista_archivos(request):
    archivos = Archivo.objects.filter(usuario=request.user)
    return render(request, 'archivo/lista_archivos.html', {'archivos': archivos})


@login_required
def subir_archivo(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.usuario = request.user  # Asocia el archivo con el usuario.
            archivo.save()
            messages.success(request, 'Archivo subido correctamente')
            return redirect('lista_archivos')  # Redirige a la lista de los archivos.
    else:
        form = ArchivoForm()
    return render(request, 'archivo/subir_archivo.html', {'form': form})


def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso')
            return redirect('lista_archivos')
    else:
        form = UserCreationForm()
    return render(request, 'archivo/registro.html', {'form': form})


def logout_usuario(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente')
    return redirect('login')


def eliminar_archivo(request, id_archivo):
    archivo = get_object_or_404(Archivo, id=id_archivo)
    
    if archivo.usuario == request.user:
        if archivo.archivo:
            # Eliminar archivo físico
            archivo.archivo.delete(save=False) 
        archivo.delete()
        messages.success(request, 'Archivo eliminado correctamente.')
        return redirect('lista_archivos')
    else:
        return HttpResponseForbidden('No se puedo eliminar el archivo.')