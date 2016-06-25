from Machine.models import *
import urllib, json
from datetime import datetime, timedelta

informacion = [
	{"url":"https://www.waze.com/row-rtserver/web/TGeoRSS?ma=600&mj=100&mu=100&left=-73.6557469367981&right=-73.59525346755981&bottom=4.1124837106779415&top=4.153986204540105&_=1450213251904",
	"ciudad":ciudad.objects.get(id = 1)}
	]

def traer_datos(url):
	response = urllib.urlopen(url)
	return json.loads(response.read())

def conv_to_date(text):
	fecha = text.split(" ")
	hora = fecha[1].split(":")
	fecha = fecha[0].split("-")
	return datetime(year=int(fecha[0]),month=int(fecha[1]),day=int(fecha[2]), hour=int(hora[0]),minute=int(hora[1]),second = int(hora[2]))

for parte in informacion:
	datos = traer_datos(parte["url"])
	startTime = conv_to_date(datos["startTime"])
	endTime = conv_to_date(datos["endTime"])
	for data in datos["alerts"]:
		try:
			lugar_id = lugar.objects.get(ciudad = parte["ciudad"], nombre = data["street"])
		except:
			id_lugar = lugar.objects.all().count()
			lugar_id = lugar.objects.create(id = id_lugar + 1, ciudad = parte["ciudad"], nombre = data["street"])
		try:
			lugar_end_id = lugar.objects.get(ciudad = parte["ciudad"], nombre = data["endNode"])
		except lugar.DoesNotExist:
			id_lugar_end = lugar.objects.all().count()
			lugar_end_id = lugar.objects.create(id = id_lugar_end + 1, ciudad = parte["ciudad"], nombre = data["endNode"])
		except KeyError:
			lugar_end_id = None
		id_evento = evento.objects.all().count()
		evento_id = evento.objects.create(
				id = id_evento + 1,
				endTimeMillis=datos["endTimeMillis"],
				startTimeMillis=datos["startTimeMillis"],
				startTime=startTime,
				endTime=endTime,
				idwaze=data["id"],
				lugar=lugar_id,
				tipo=data["type"]
			)
		id_punto = punto.objects.all().count()
		p = punto.objects.create(
				id = id_punto + 1,
				evento = evento_id,
				latitud = data["location"]["y"],
				longitud = data["location"]["x"]
			)
		id_alerta = alerta.objects.all().count()
		try:
			reportDescription = data["reportDescription"]
		except KeyError:
			reportDescription = ""
		a = alerta(
				descripcion = reportDescription,
				subtipo = data["subtype"],
				confiabilidad = data["reliability"],
				evento = evento_id,
				pubMillis = data["pubMillis"],
			)
		a.save()
	for data in datos["jams"]:
		try:
			lugar_id = lugar.objects.get(ciudad = parte["ciudad"], nombre = data["street"])
		except:
			id_lugar = lugar.objects.all().count()
			lugar_id = lugar.objects.create(id = id_lugar + 1, ciudad = parte["ciudad"], nombre = data["street"])
		try:
			lugar_end_id = lugar.objects.get(ciudad = parte["ciudad"], nombre = data["endNode"])
		except lugar.DoesNotExist:
			id_lugar_end = lugar.objects.all().count()
			lugar_end_id = lugar.objects.create(id = id_lugar_end + 1, ciudad = parte["ciudad"], nombre = data["endNode"])
		except KeyError:
			lugar_end_id = None
		id_evento = evento.objects.all().count()
		evento_id = evento.objects.create(
				id = id_evento + 1,
				endTimeMillis=datos["endTimeMillis"],
				startTimeMillis=datos["startTimeMillis"],
				startTime=startTime,
				endTime=endTime,
				idwaze=data["id"],
				lugar=lugar_id,
				tipo=data["type"]
			)
		for coordenadas in data["line"]:
			id_punto = punto.objects.all().count()
			p = punto.objects.create(
					id = id_punto + 1,
					evento = evento_id,
					latitud = coordenadas["y"],
					longitud = coordenadas["x"]
				)
		try:
			blockingAlertUuid = data["blockingAlertUuid"]
		except KeyError:
			blockingAlertUuid = ""
		id_trancon = trancon.objects.all().count()
		t = trancon(
				id = id_trancon + 1,
				severidad=data["severity"],
				nivel=data["level"],
				longitud=data["length"],
				lugarend=lugar_end_id,
				velocidad=data["speed"],
				alerta=blockingAlertUuid,
				evento=evento_id,
				pubMillis=data["pubMillis"]
			)
		t.save()
		# pais.objects.create(id = 2, nombre = data["country"])



