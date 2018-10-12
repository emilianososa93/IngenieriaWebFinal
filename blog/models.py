from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User
import os

class Post(models.Model):
    idpublicion = models.ForeignKey(User,on_delete = models.CASCADE, null=True,blank=True, default='')
    idseccion = models.TextField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, default='')
    apellido = models.CharField(max_length=50, null=False, blank=False, default='')
    email = models.EmailField(max_length=50)
    usuario = models.OneToOneField(User,on_delete = models.CASCADE, null=True, blank=True)
    fechanacimiento = models.DateField(null=True, blank=True)
    tokenActivacion = models.CharField(max_length = 40, blank = True, null = True)

    def __str__(self):
        return self.usuario.username

class Secciones(models.Model):
    idseccion = models.AutoField(primary_key = True, null=False, blank=True)
    descripcion = models.TextField(max_length=50)   
    def __str__(self):
        return self.idseccion 



class Comentario(models.Model):  
    idpublicion = models.ForeignKey(Post,on_delete = models.CASCADE, null=True, blank=True)
    cuerpocomentario = models.TextField(null=False, blank=True)
    idusuario = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)  
    fechaBaja = models.DateTimeField(auto_now=False, null=True,blank=True,default=None)
    fechaAlta = models.DateTimeField(auto_now=False, null=True,blank=True, default=None)

    def __str__(self):
        return self.cuerpocomentario

class MotivoDenuncia(models.Model):
    motivo = models.TextField(null=True,blank=False)

    def __str__(self):
        return self.motivo


class Denuncias(models.Model):
    idusuario = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)  
    idcomentario = models.ForeignKey(Comentario,on_delete = models.CASCADE, null=True, blank=True)
    fechadenuncia = models.DateTimeField(auto_now=False, null=True, blank=True, default=None)
    idmotivo = models.ForeignKey(MotivoDenuncia, on_delete = models.CASCADE,null=True, blank=False)
    idpublicion = models.ForeignKey(Post,on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.idusuario)


