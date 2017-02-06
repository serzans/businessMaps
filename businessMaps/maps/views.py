from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

def index(request):
	test_variable="Test variable to be passed to a map."
	template=loader.get_template('maps/index.html')
	context={
		'test_variable': test_variable,
	}
	return render(request,"maps/index.html",context)
	# return HttpResponse("Hello, world.")