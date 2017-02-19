from django.shortcuts import render
from django.template import loader


# Google maps API example
from django.conf import settings

GMAPS_API_KEY=getattr(settings,"GMAPS_API_KEY",None)

import googlemaps

gmaps=googlemaps.Client(key=GMAPS_API_KEY)

address = 'Lady Margaret Hall'
result = gmaps.geocode(address)

lat = result[0][u'geometry'][u'location'][u'lat']
lng = result[0][u'geometry'][u'location'][u'lng']


# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)

# End of Google maps exmaple

query = 'restaurant' # type of business user inputted
rad = 100 # depends on the zoom level
places = gmaps.places(query, location = (lat, lng), radius = rad)

geojson = []
for place in places['results']:
	geo_dict = {}
	geo_dict['type'] = 'Feature'
	geo_dict['geometry'] = {}
	geo_dict['geometry']['type'] = 'Point'
	geo_dict['geometry']['coordinates'] = place['geometry']['location'].values()
	geo_dict[u'type'] = 'Feature'
	geo_dict[u'geometry'] = {}
	geo_dict[u'geometry'][u'type'] = 'Point'
	geo_dict[u'geometry'][u'coordinates'] = place[u'geometry'][u'location'].values()

	geojson.append(geo_dict)

from django.http import HttpResponse

def index(request):
	test_variable='Test string to pass to the template'
	template=loader.get_template('maps/index.html')
	context={
		'test_variable': test_variable,
		'lat': lat,
		'lng': lng,
		'geojson': geojson,
	}
	return render(request,"maps/index.html",context)
	# return HttpResponse("Hello, world.")

# latest
