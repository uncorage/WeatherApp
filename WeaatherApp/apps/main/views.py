from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def index(request):
    if request.method == 'POST':
        city = request.replace(" ","+")
        response = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
        soup = BeautifulSoup(response.text,'html.parser')

        data = {
            'location': soup.select('#wob_loc')[0].getText().strip(),  
            'time': soup.select('#wob_dts')[0].getText().strip(),
            'info': soup.select('#wob_dc')[0].getText().strip(),
            'weather': soup.select('#wob_tm')[0].getText().strip(),
        }

        return(data['location'])
        return(data['time'])
        return(data['info'])
        return(data['weather']+"°C") 
    
    else:
        data = {}
            
        return render(request, "main/index.html", data)