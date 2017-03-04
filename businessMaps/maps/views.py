from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView

# Google maps API example
from django.conf import settings
import json

from . import models
from django.http import HttpResponse

def index(request):
	gmaps = models.MapRequest().g_maps()
	test_variable='Test string to pass to the template'
	template=loader.get_template('maps/index.html')
	context={
		'test_variable': test_variable,
		'lat': gmaps.lat,
		'lng': gmaps.lng,
		'geojson': gmaps.geolist,
	}

	return render(request,"maps/index.html",context)
	# return HttpResponse("Hello, world.")

def ajax(request):
	gmaps = models.MapRequest().g_maps()
	geojson = json.dumps(gmaps.geolist)
	return HttpResponse(geojson, content_type = 'application/json') 
# latest

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
