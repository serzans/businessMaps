from __future__ import unicode_literals

from django.db import models
from django.conf import settings

import googlemaps

# Create your models here.

class TestEntry(models.Model):
	test_text=models.CharField(max_length=200)
	def __str__(self):
		return self.test_text

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

class MapRequest(models.Model):

	def __init__(self):
		self.key = getattr(settings,"GMAPS_API_KEY",None)
	
	def g_maps(self, query = 'restaurant',
				rad = 100, address = 'Lady Margaret Hall'
				):
		gmaps = googlemaps.Client(key=self.key)
		result = gmaps.geocode(address)

		self.lat = result[0][u'geometry'][u'location'][u'lat']
		self.lng = result[0][u'geometry'][u'location'][u'lng']

		places = gmaps.places(query, location = (self.lat, self.lng), radius = rad)

		geolist = []
		for place in places[u"results"]:
			geo_dict = {}
			geo_dict[u"type"] = "Feature"
			geo_dict[u"geometry"] = {}
			geo_dict[u"geometry"][u"type"] = "Point"
			geo_dict[u"geometry"][u"coordinates"] = list(place[u"geometry"][u"location"].values())[::-1]

			geo_dict[u"properties"] = {}
			geo_dict[u"properties"][u"title"] = place[u"name"]
			geo_dict[u"properties"][u"icon"] = "monument"

			geolist.append(geo_dict)

		self.geolist = geolist

		return self

