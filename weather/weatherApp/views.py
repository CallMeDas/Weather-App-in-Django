from django.shortcuts import render
import datetime
import requests
from django.contrib import messages

# Create your views here.

def home(request):
    city = 'kathmandu'
    
    if request.method == 'POST':
        city = request.POST.get('city', 'kathmandu')
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0a4e944ce1a6cf3f9a709eb8d4838501'
    params = {'units': 'metric'}

    API_KEY =  'AIzaSyAqCLrAGqd3BTXd3woNJDMZP78WKasa_QM'

    SEARCH_ENGINE_ID = '8046ab450deef4e67'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']

    response = requests.get(url, params=params).json()
    
    if response['cod'] == 200:
        cont = {
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
            'temp': response['main']['temp'],
            'day': datetime.date.today(),
            'city': response['name'],
            'image_url':image_url
        }
    else:
        exception_occurred = True
        messages.error(request,'Entered data is not available to API')
        cont = {
            'error': "City not found.",
            'day': datetime.date.today(),
            'exception_occurred':exception_occurred 
        }
           

    return render(request, 'index.html', cont)
