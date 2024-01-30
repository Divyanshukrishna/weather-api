from django.shortcuts import render
import urllib.request
import json
# Create your views here.

def home(request):
    data={}
    if request.method == 'POST':
        city = request.POST['city']
        lang = request.POST['lang']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=' + lang + '&appid=7e78767fc65fdb0b6643f2d2b1f581dc').read()
        list_of_data=json.loads(source)
        data={
            "country_code":str(list_of_data['sys']['country']),
            "coordinate":str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
            "temp":str(list_of_data['main']['temp']) +'C',
            "pressure":str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main":str(list_of_data['weather'][0]['main']),
            "description":str(list_of_data['weather'][0]['description']),
            "icon":list_of_data['weather'][0]['icon'],
        }
        print(data)
    return render(request,"index.html",data)
