from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kathmandu'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0a4e944ce1a6cf3f9a709eb8d4838501'
    PARAMS = {'units' : 'metric'}

    data = request.get(url, PARAMS).json()
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp =data['main']['temp']
    day = datetime.date.today()

    cont = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day' : day
    }


    return render(request,'index.html', cont)
