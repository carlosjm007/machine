from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from sklearn import datasets, svm, metrics
from PIL import Image
from io import BytesIO
from Machine.models import *
import base64, numpy, cv2, urllib, json

classifier = svm.SVC(gamma=0.00000001)
imagenes = []
objetivos = []

def Marla(request):
	html = "<html><body>Vas a poder con todo amor, eres la mejor :*</body></html>"
	return HttpResponse(html)

def dinamica(request):
	html = "<html><body>Dinamica Solidaria</body></html>"
	return HttpResponse(html)

def granadilla(request):
	html = "<html><body>Los quiero a todos pandilla granadilla, malparidos</body></html>"
	return HttpResponse(html)

def Inicio(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def trafico(request):
	url = "https://www.waze.com/row-rtserver/web/TGeoRSS?ma=600&mj=100&mu=100&left=-73.6557469367981&right=-73.59525346755981&bottom=4.1124837106779415&top=4.153986204540105&_=1450213251904"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return JsonResponse(data ,safe = False)

@csrf_protect
def foto(request):
	if request.method == 'POST':
		# d = request.POST["foto"]
		# file_like = Image.open(BytesIO(base64.b64decode(d)))
		# img = cv2.cvtColor(numpy.array(file_like), cv2.COLOR_BGR2GRAY)
		# _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	
		imagenes.append(request.POST["foto"])
		objetivos.append(request.POST["objetivo"])

		return JsonResponse({"foto":len(imagenes)}, safe=True)

def encajar(request):
	imge=[]
	for u in range(len(imagenes)):
		file_like = Image.open(BytesIO(base64.b64decode(imagenes[u])))
		img = cv2.cvtColor(numpy.array(file_like), cv2.COLOR_BGR2GRAY)
		_, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
		imge.append(img)
	n_samples = len(imge)
	image = numpy.array(imge)
	data = image.reshape((n_samples, -1))
	classifier.fit(data, objetivos)
	return JsonResponse({"foto":"ok", "len":len(imagenes)}, safe=True)

@csrf_protect
def predecir(request):
	if request.method == 'POST':
		imge = []
		d = request.POST["foto"]
		file_like = Image.open(BytesIO(base64.b64decode(d)))
		img = cv2.cvtColor(numpy.array(file_like), cv2.COLOR_BGR2GRAY)
		_, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
		imge.append(img)
		n_samples = len(imge)
		image = numpy.array(imge)
		data = image.reshape((n_samples, -1))
		predicted = classifier.predict(data)
		return JsonResponse({"foto":predicted[0]}, safe=True)

def reset(request):
	global classifier
	classifier = svm.SVC(gamma=0.00000001)
	global imagenes
	imagenes = []
	
	global objetivos
	objetivos = []
	return JsonResponse({"respuesta":True}, safe=True)

def vista_trafico(request):
	return render_to_response('trafico.html',context_instance=RequestContext(request))