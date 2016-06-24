# -*- coding: utf-8 -*-
import psycopg2, urllib, json, sys
from datetime import datetime, timedelta
def traer_datos():
	url = "https://www.waze.com/row-rtserver/web/TGeoRSS?ma=600&mj=100&mu=100&left=-73.6557469367981&right=-73.59525346755981&bottom=4.1124837106779415&top=4.153986204540105&_=1450213251904"
	response = urllib.urlopen(url)
	return json.loads(response.read())

def conv_to_date(text):
	fecha = text.split(" ")
	hora = fecha[1].split(":")
	fecha = fecha[0].split("-")
	return datetime(year=int(fecha[0]),month=int(fecha[1]),day=int(fecha[2]), hour=int(hora[0]),minute=int(hora[1]),second = int(hora[2]))

try:
	con = psycopg2.connect(
		database='rutas',
		user='carlosjm5',
		host='ec2-52-11-218-51.us-west-2.compute.amazonaws.com',
		password='renault+4')
	# con = psycopg2.connect(
	# 	database='rutas',
	# 	user='postgres',
	# 	host='localhost',
	# 	password='111111')
	cur = con.cursor()
	datos = traer_datos()
	print None, datos["endTimeMillis"]

	endTimeMillis = datos["endTimeMillis"]
	startTimeMillis = datos["startTimeMillis"]
	startTime = conv_to_date(datos["startTime"])
	endTime = conv_to_date(datos["endTime"])

	for data in datos["jams"]:
		cur.execute("select * from pais where nombre = '" + data["country"] + "'")
		if cur.fetchone() == None:
			cur.execute("select count(*) from pais")
			pais_id = cur.fetchone()[0]
			cur.execute("insert into pais (id, nombre) values (%s,%s)",((pais_id + 1),data["country"]))
			con.commit()
			print "no hay pais", pais_id
		else:
			cur.execute("select * from pais where nombre = '" + data["country"] + "'")
			pais_id = cur.fetchone()[0]
			print "si hay pais", pais_id

		cur.execute("select * from ciudad where nombre = '" + data["city"] + "' and  pais_id ='" + str(pais_id) + "'")
		if cur.fetchone() == None:
			cur.execute("select count(*) from ciudad")
			ciudad_id = cur.fetchone()[0]
			cur.execute("insert into ciudad (id, nombre,pais_id) values (%s,%s,%s)",((ciudad_id + 1),data["city"], str(pais_id)))
			con.commit()
			print "no hay ciudad", ciudad_id
		else:
			cur.execute("select * from ciudad where nombre = '" + data["city"] + "'")
			ciudad_id = cur.fetchone()[0]
			print "si hay ciudad", ciudad_id

		cur.execute("select * from lugar where nombre = '" + data["street"] + "' and  ciudad_id ='" + str(ciudad_id) + "'")
		if cur.fetchone() == None:
			cur.execute("select count(*) from lugar")
			lugar_id = cur.fetchone()[0]
			cur.execute("insert into lugar (id, nombre,ciudad_id) values (%s,%s,%s)",((lugar_id + 1),data["street"], str(ciudad_id)))
			con.commit()
			print "no hay lugar", lugar_id
		else:
			cur.execute("select * from lugar where nombre = '" + data["street"] + "'")
			lugar_id = cur.fetchone()[0]
			print "si hay lugar", lugar_id

		try:
			blockType = data["blockType"]
		except:
			blockType = "JAM"
		# Guardar cada trancon

	for data in datos["alerts"]:
		cur.execute("select * from pais where nombre = '" + data["country"] + "'")
		if cur.fetchone() == None:
			cur.execute("select count(*) from pais")
			pais_id = cur.fetchone()[0]
			cur.execute("insert into pais (id, nombre) values (%s,%s)",((pais_id + 1),data["country"]))
			con.commit()
			print "no hay pais", pais_id
		else:
			cur.execute("select * from pais where nombre = '" + data["country"] + "'")
			pais_id = cur.fetchone()[0]
			print "si hay pais", pais_id

		cur.execute("select * from ciudad where nombre = '" + data["city"] + "' and  pais_id ='" + str(pais_id) + "'")
		if cur.fetchone() == None:
			cur.execute("select count(*) from ciudad")
			ciudad_id = cur.fetchone()[0]
			cur.execute("insert into ciudad (id, nombre,pais_id) values (%s,%s,%s)",((ciudad_id + 1),data["city"], str(pais_id)))
			con.commit()
			print "no hay ciudad", ciudad_id
		else:
			cur.execute("select * from ciudad where nombre = '" + data["city"] + "'")
			ciudad_id = cur.fetchone()[0]
			print "si hay ciudad", ciudad_id

		cur.execute("select * from lugar where nombre = '" + data["street"] + "' and  ciudad_id ='" + str(ciudad_id) + "'")
		if cur.fetchone() == None:
			cur.execute("select count(*) from lugar")
			lugar_id = cur.fetchone()[0]
			cur.execute("insert into lugar (id, nombre,ciudad_id) values (%s,%s,%s)",((lugar_id + 1),data["street"], str(ciudad_id)))
			con.commit()
			print "no hay lugar", lugar_id
		else:
			cur.execute("select * from lugar where nombre = '" + data["street"] + "'")
			lugar_id = cur.fetchone()[0]
			print "si hay lugar", lugar_id

		# Guardar cada punto

except psycopg2.DatabaseError, e:
	print 'Error %s' % e
	sys.exit(1)