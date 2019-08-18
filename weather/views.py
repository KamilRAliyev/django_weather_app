from django.shortcuts import render
import requests
import json
from .models import City
from .forms import CityForm
# Create your views here.


def index(request):
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm

    cities = City.objects.all()
    allCities=[]
    for city in cities:
        dic = {
            'appid' : '17a0af686c6c48d3ea94d17e2b507e75',
            'q' : city.name,
            'units':'metric',
        }
        url = 'https://api.openweathermap.org/data/2.5/weather'
        res = requests.get(url, params=dic).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'country': res['sys']['country'],
            'pressure': res['main']['pressure']
        }
        allCities.append(city_info)

    context = {'all_info': allCities,
               'form': form}
    
    return render(request, 'weather/index.html', context)