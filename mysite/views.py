from django.utils import timezone
from .forms import PostForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login, authenticate, get_user_model,logout
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render , redirect, get_object_or_404


def post_portada(request):
    if request.method == "POST":
        form = PostForm(request.POST)
    else:
        form = PostForm()
    return render(request, 'blog/post_portada.html', {'form': form})



def post_login(request):

    url_next = request.GET.get('next', None) 
    if request.method == "POST":
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if url_next is not None:
                return HttpResponseRedirect(url_next)
            else:
                return HttpResponseRedirect('/') 
        else:
            messages.success(request, "Usuario/contraseña ingresado invalido") 
    else:
        form = UserForm(request.POST)
    return render(request, 'blog/post_login.html', {'form': form})



def post_logout(request):
    logout(request)
    return HttpResponseRedirect('/post/portada/')

def post_confirmar(request, tokenActivacion):
    usuario  = get_object_or_404(Usuario, tokenActivacion = tokenActivacion )    
    user = usuario.usuario
    user.is_active  = True
    user.save()
    return render(request, 'blog/post_bienvenida.html',context={'nombre_usuario': user.first_name},
)