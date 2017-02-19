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


from django.http import HttpResponse

def index(request):
	test_variable='Test string to pass to the template'
	template=loader.get_template('maps/index.html')
	context={
		'test_variable': test_variable,
		'lat': lat,
		'lng': lng,
	}
	return render(request,"maps/index.html",context)
	# return HttpResponse("Hello, world.")

