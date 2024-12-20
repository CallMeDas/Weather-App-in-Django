from django.shortcuts import render
import datetime
import requests

# Create your views here.

def home(request):
    city = 'kathmandu'
    
    if request.method == 'POST':
        city = request.POST.get('city', 'kathmandu')
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0a4e944ce1a6cf3f9a709eb8d4838501'
    params = {'units': 'metric'}

    response = requests.get(url, params=params).json()
    
    if response['cod'] == 200:
        cont = {
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
            'temp': response['main']['temp'],
            'day': datetime.date.today(),
            'city': response['name'],
        }
    else:
        cont = {
            'error': "City not found.",
            'day': datetime.date.today(),
        }

    return render(request, 'index.html', cont)
