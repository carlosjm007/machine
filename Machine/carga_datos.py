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
	# for data in datos["jams"]:
	# cur.execute("insert into ciudad (nombre, ciudad_id) values (%s,%s)",("Villavo","Colombi"))
	# con.commit()
	datos = traer_datos()
	fecha = conv_to_date(datos["endTime"]) - timedelta(hours = 5)
	for data in datos["jams"]:
		delta = data["updateMillis"] - datos["startTimeMillis"]
		actualizado =fecha + timedelta(milliseconds = delta)
		try:
			print actualizado, fecha, actualizado - fecha, data["street"].encode('utf8')
		except:
			pass
		# cur.execute("select * from pais where nombre = '" + data["country"] + "'")
		# if cur.fetchone() == None:
		# 	cur.execute("select count(*) from pais")
		# 	pais_id = cur.fetchone()[0]
		# 	cur.execute("insert into pais (id, nombre) values (%s,%s)",((pais_id + 1),data["country"]))
		# 	con.commit()
		# 	print "no hay pais", pais_id
		# else:
		# 	cur.execute("select * from pais where nombre = '" + data["country"] + "'")
		# 	pais_id = cur.fetchone()[0]
		# 	print "si hay pais", pais_id

		# cur.execute("select * from ciudad where nombre = '" + data["city"] + "' and  pais_id ='" + str(pais_id) + "'")
		# if cur.fetchone() == None:
		# 	cur.execute("select count(*) from ciudad")
		# 	ciudad_id = cur.fetchone()[0]
		# 	cur.execute("insert into ciudad (id, nombre,pais_id) values (%s,%s,%s)",((ciudad_id + 1),data["city"], str(pais_id)))
		# 	con.commit()
		# 	print "no hay ciudad", ciudad_id
		# else:
		# 	cur.execute("select * from ciudad where nombre = '" + data["city"] + "'")
		# 	ciudad_id = cur.fetchone()[0]
		# 	print "si hay ciudad", ciudad_id

		# cur.execute("select * from lugar where nombre = '" + data["street"] + "' and  ciudad_id ='" + str(ciudad_id) + "'")
		# if cur.fetchone() == None:
		# 	cur.execute("select count(*) from lugar")
		# 	lugar_id = cur.fetchone()[0]
		# 	cur.execute("insert into lugar (id, nombre,ciudad_id) values (%s,%s,%s)",((lugar_id + 1),data["street"], str(ciudad_id)))
		# 	con.commit()
		# 	print "no hay lugar", lugar_id
		# else:
		# 	cur.execute("select * from lugar where nombre = '" + data["street"] + "'")
		# 	lugar_id = cur.fetchone()[0]
		# 	print "si hay lugar", lugar_id

	'''
	datos = traer_datos()
	u = datetime.today()
	for data in datos["jams"]:
		try:
			cur.execute("insert into pais (nombre) values ('" + data["country"] + "')")
			con.commit()
		except psycopg2.DatabaseError, e:
			con.rollback()
			print 'Error1 %s' % e 

		try:
			cur.execute("insert into ciudad (nombre, pais_id) values ('" + data["city"] + "','" + data["country"] + "')")
			con.commit()
		except psycopg2.DatabaseError, e:
			con.rollback()
			print 'Error2 %s' % e

		try:
			cur.execute("insert into lugar (nombre, ciudad_id) values ('" + data["street"] + "','" + data["city"] + "')")
			con.commit()
		except psycopg2.DatabaseError, e:
			con.rollback()
			print 'Error3 %s' % e

		try:
			cur.execute("select count(*) from velocidad")
			numero = cur.fetchone()[0]
			print numero, str(data["street"])
			cur.execute("insert into velocidad (id, fecha, velocidad, lugar_id) values ('" + str(numero + 1) + "','" + u.strftime("%Y-%m-%d %H:%M:%S") + "','" + str(data["speed"]) + "','" + str(data["street"]) + "')")
			con.commit()
			for linea in data["line"]:
				cur.execute("insert into coordenada (velocidad_id, latitud, longitud) values ('" + str(numero + 1) + "','" + str(linea["y"]) + "','" + str(linea["x"]) + "')")
				con.commit()
		except psycopg2.DatabaseError, e:
			con.rollback()
			print 'Error4 %s' % e

	print len(datos["jams"]),datos["jams"][0]["city"],datos["jams"][0]["country"]
	'''
except psycopg2.DatabaseError, e:
	print 'Error %s' % e
	sys.exit(1)