from django.db import models
from django.contrib.auth.models import User

class pais(models.Model):
	nombre = models.CharField(max_length = 200)
	class Meta:
		db_table = 'pais'
	def __unicode__(self):
		return self.nombre

class ciudad(models.Model):
	nombre = models.CharField(max_length = 200)
	pais = models.ForeignKey(pais)
	class Meta:
		db_table = 'ciudad'
	def __unicode__(self):
		return self.nombre

class lugar(models.Model):
	nombre = models.CharField(max_length = 200)
	ciudad = models.ForeignKey(ciudad)
	class Meta:
		db_table = 'lugar'
	def __unicode__(self):
		return self.nombre

class evento(models.Model):
	endTimeMillis = models.CharField(max_length = 15, db_tablespace= "endTimeMillis")
	startTimeMillis = models.CharField(max_length = 15, db_tablespace= "startTimeMillis")
	startTime = models.DateTimeField(db_tablespace= "startTime")
	endTime = models.DateTimeField(db_tablespace= "endTime")
	creado = models.DateTimeField(db_tablespace= "creado", auto_now = True)
	idwaze = models.CharField(max_length = 200, db_tablespace= "idwaze")
	lugar = models.ForeignKey(lugar)
	tipo = models.CharField(max_length = 100, db_tablespace= "tipo")
	class Meta:
		db_table = 'evento'
	def __unicode__(self):
		return self.lugar.nombre

class punto(models.Model):
	evento = models.ForeignKey(evento)
	latitud = models.FloatField(max_length=45, db_tablespace= "latitud")
	longitud = models.FloatField(max_length=45, db_tablespace= "longitud")
	class Meta:
		db_table = 'punto'
	def __unicode__(self):
		return self.evento.lugar.nombre

class alerta(models.Model):
	descripcion = models.CharField(max_length = 200, db_tablespace= "descripcion")
	subtipo = models.CharField(max_length = 100, db_tablespace= "subtipo")
	confiabilidad = models.CharField(max_length = 10, db_tablespace= "confiabilidad")
	evento = models.OneToOneField(evento)
	pubMillis = models.CharField(max_length = 15, db_tablespace= "pubMillis")
	class Meta:
		db_table = 'alerta'
	def __unicode__(self):
		return self.evento.lugar.nombre

class trancon(models.Model):
	severidad = models.CharField(max_length = 3, db_tablespace= "severidad")
	nivel = models.CharField(max_length = 3, db_tablespace= "nivel")
	longitud = models.CharField(max_length = 45, db_tablespace= "longitud")
	lugarend = models.ForeignKey(lugar, blank=True, null=True, related_name='lugarend')
	velocidad = models.CharField(max_length = 50, db_tablespace= "velocidad")
	alerta = models.CharField(max_length = 200, db_tablespace= "alerta")
	lugarstart = models.ForeignKey(lugar, blank=True, null=True, related_name='lugarstart')
	evento = models.OneToOneField(evento)
	pubMillis = models.CharField(max_length = 15, db_tablespace= "pubMillis")
	class Meta:
		db_table = 'trancon'
	def __unicode__(self):
		return self.evento.lugar.nombre