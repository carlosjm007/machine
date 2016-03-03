from django.db import models
from django.contrib.auth.models import User

class pais(models.Model):
	nombre = models.CharField(max_length = 200, primary_key=True)
	class Meta:
		db_table = 'pais'
	def __unicode__(self):
		return self.nombre
		

class ciudad(models.Model):
	nombre = models.CharField(max_length = 200, primary_key=True)
	pais = models.ForeignKey(pais)
	class Meta:
		db_table = 'ciudad'
	def __unicode__(self):
		return self.nombre

class lugar(models.Model):
	nombre = models.CharField(max_length = 200, primary_key=True)
	ciudad = models.ForeignKey(ciudad)
	class Meta:
		db_table = 'lugar'
	def __unicode__(self):
		return self.nombre

class velocidad(models.Model):
	fecha = models.DateTimeField(db_tablespace= "fecha", auto_now = True)
	velocidad = models.CharField(max_length = 45, db_tablespace= "velocidad")
	lugar = models.ForeignKey(lugar)
	class Meta:
		db_table = 'velocidad'
	def __unicode__(self):
		return self.lugar.nombre

class coordenada(models.Model):
    velocidad = models.ForeignKey(velocidad)
    latitud = models.FloatField(max_length=45, db_tablespace= "latitud")
    longitud = models.FloatField(max_length=45, db_tablespace= "longitud")
    class Meta:
        db_table = 'coordenada'
    def __unicode__(self):
        return self.velocidad