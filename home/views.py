from django.shortcuts import render
import urllib.request
import json,requests

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        source =  'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1' 
        city_weather = requests.get(source.format(city)).json()
        data = {
            "country": city,
            "weather_temperature": city_weather['main']['temp'],
            "weather_pressure": city_weather['main']['pressure'],
            "weather_humidity": city_weather['main']['humidity'],
            "weather_icon": city_weather['weather'][0]['icon'],
        }
        context = {
                "city": city,
                "data": data,
        }
    else:
        data ={}
    return render(request, 'home.html',context)