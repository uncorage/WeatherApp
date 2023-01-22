from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def index(request):
    if request.method == 'POST':
        print(request.POST)
        city = request.POST['city'].replace(" ","")
        city = city+" Weathers"
        print(city)
        response = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
        # print(response.content)
        soup = BeautifulSoup(response.text,'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip() 
        time = soup.select('#wob_dts')[0].getText().strip(),
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()

        data = {
            'location': location,  
            'time': time,
            'info': info,
            'weather': f"{weather}C",
        }
        print(data)

        # return HttpResponse(data)
    
    else:
        data = {}
            
    return render(request, "main/index.html", data)