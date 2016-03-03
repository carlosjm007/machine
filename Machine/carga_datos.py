#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2, urllib, json, sys
from datetime import datetime
def traer_datos():
	url = "https://www.waze.com/row-rtserver/web/TGeoRSS?ma=600&mj=100&mu=100&left=-73.6557469367981&right=-73.59525346755981&bottom=4.1124837106779415&top=4.153986204540105&_=1450213251904"
	response = urllib.urlopen(url)
	return json.loads(response.read())

try:
	con = psycopg2.connect(
		database='rutas',
		user='carlosjm5',
		host='ec2-52-36-4-76.us-west-2.compute.amazonaws.com',
		password='renault+4') 
	cur = con.cursor()
	# for data in datos["jams"]:
	# cur.execute("insert into ciudad (nombre, ciudad_id) values (%s,%s)",("Villavo","Colombi"))
	# con.commit()
	# cur.execute("select count(*) from velocidad")
	# print cur.fetchone()[0]
	
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
			print numero
			cur.execute("insert into velocidad (id, fecha, velocidad, lugar_id) values ('" + str(numero + 1) + "','" + u.strftime("%Y-%m-%d %H:%M:%S") + "','" + str(data["speed"]) + "','" + str(data["street"]) + "')")
			con.commit()
			for linea in data["line"]:
				cur.execute("insert into coordenada (velocidad_id, latitud, longitud) values ('" + str(numero + 1) + "','" + str(linea["y"]) + "','" + str(linea["x"]) + "')")
				con.commit()
		except psycopg2.DatabaseError, e:
			con.rollback()
			print 'Error4 %s' % e

	print len(datos["jams"]),datos["jams"][0]["city"],datos["jams"][0]["country"]

except psycopg2.DatabaseError, e:
	print 'Error %s' % e
	sys.exit(1)