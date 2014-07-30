from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context,loader
from content.models import Cities, Languages, Activities

# Create your views here.
def index(request):
	template = loader.get_template('index.html')
	context = Context({
	})
	return HttpResponse(template.render(context))


def search(request,query=""):
	# send to view 
	template = loader.get_template('search.html') 

	sql = "SELECT distinct * FROM content_cities WHERE id>13 AND name LIKE '%"+query+"%' OR description LIKE '%"+query+"%'"
	c = Cities.objects.raw(sql) 
	sql = "SELECT distinct * FROM content_activities WHERE name LIKE '%"+query+"%' OR description LIKE '%"+query+"%'"
	a = Activities.objects.raw(sql) 
	sql = "SELECT distinct * FROM content_languages WHERE name LIKE '%"+query+"%' OR description LIKE '%"+query+"%'"
	l = Languages.objects.raw(sql) 

	if(query==""):
		context = Context({
			'blank':True, 
		})
	else: 
		context = Context({
			'blank':False, 
			'query':query,
			'cities':c, 
			'ccount':len(list(c)),  
			'cbool':len(list(c))>0, 
			'activities':a, 
			'acount':len(list(a)),  
			'abool':len(list(a))>0, 
			'languages':l, 
			'lcount':len(list(l)),  
			'lbool':len(list(l))>0, 
		})

	return HttpResponse(template.render(context))


# --------------
#	apis
# --------------
def api(request):
	template = loader.get_template('api.html') 
	context = Context({
		'type':'all', 
	})
	return HttpResponse(template.render(context))

# --------------
#	cities
# --------------
def api_cities(request,city_id=None):
	all_cities = False 

	# get city by city_id type 
	if(city_id!=None): 
		if city_id.isdigit():
			# city_id is an int, thus an id 
			city = Cities.objects.get(id=city_id) 
		else:
			# city_id is a string, thus a name 
			city = Cities.objects.get(name=city_id) 
	else: 
		# city_id is empty, so they want all cities 
		all_cities = True 
		city = Cities.objects.all() 

	# generate json string 
	if all_cities:
		json_city = '[{"id":0,"name":"City Name 1"},{"id":1,"name":"City Name 2"}]'
	else: 
		json_city = '{"id":0,"name":"City Name 1"}' 

	# send to view 
	template = loader.get_template('api.html') 
	context = Context({
		'json_str':json_city,
	})
	return HttpResponse(template.render(context))


# --------------
#	languages
# --------------
def api_languages(request,lang_id=-1):
	template = loader.get_template('api.html') 
	context = Context({
		'type':'languages', 
		'lang_id':lang_id, 
	})
	return HttpResponse(template.render(context))


# --------------
#	activities 
# --------------
def api_activities(request,acts_id=-1):
	template = loader.get_template('api.html') 
	context = Context({
		'type':'activities', 
		'acts_id':acts_id, 
	})
	return HttpResponse(template.render(context))
