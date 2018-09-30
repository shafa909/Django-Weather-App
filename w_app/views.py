from django.shortcuts import render
import requests
import datetime



def index(request):

	url          = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=de1ad726b02e26193a38665f1b1f274f'
	city         = 'Bangalore'
	city_weather = requests.get(url.format(city)).json()
	weather = {
	       'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

	datetime1 = datetime.datetime.now() 
   
	context = {'weather' : weather, 'datetime':datetime1}    
	print(city_weather)
	return render(request, 'w_app/index.html' , context) 
