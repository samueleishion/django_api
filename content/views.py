from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context,loader
from content.models import Cities
from content.models import Languages
from content.models import Activities

# Create your views here.
def index(request):
	template = loader.get_template('index.html')
	context = Context({
	})
	return HttpResponse(template.render(context))

def api(request):
	c = Cities.objects.create(name="dummy") 
	# error = False 
	# if(c.name=="dummy"): 
	# 	error = True

	all_cities = Cities.objects.all() 
	template = loader.get_template('api.html')
	context = Context({
		'cities':all_cities,
		'test_city':c, 
		# 'error':error, 
	})
	return HttpResponse(template.render(context))