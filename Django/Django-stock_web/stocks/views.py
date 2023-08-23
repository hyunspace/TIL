from django.shortcuts import render
import requests
import json
import secret
from django.http import HttpResponse

# Create your views here.

def home(request):

    try:
        ticker = request.GET['ticker']
        stock_api = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=" + secret.API_TOKEN)
        stock = json.loads(stock_api.content)

    except Exception as e:
        stock = ""

    content = {'stock': stock}

    return render(request, 'home.html', content)