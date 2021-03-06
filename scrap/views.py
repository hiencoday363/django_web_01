from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import date
import requests, json

from scrap.bs4_scrap import *

# Create your views here.

today = date.today().strftime("%A-%d-%m-%Y")

url_tem = 'http://api.openweathermap.org/data/2.5/weather?appid=09a71427c59d38d6a34f89b47d75975c&q=hanoi&units=metric'
result = requests.get(url_tem)
json_temp = result.json()
if json_temp['cod'] != '404':
  temp = json_temp['main']['temp']
else:
  temp = None


def pagination(data,request):
  paginator = Paginator(data, 7) 
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  try:
    request.COOKIES['sessionid']
    isLogin = True
  except:
    isLogin = False

  data = {'data': page_obj, 'date':today, 'temp':temp, 'isLogin': isLogin}

  return data

def home(request):
  data = news()
  result = pagination(data,request) 

  return render(request, 'scrap/home.html', result)

def tech(request):
  data = technology_news()
  result = pagination(data,request) 
  result['nav'] = 'technology'

  return render(request, 'scrap/home.html', result)

def business(request):
  data = business_news()
  result = pagination(data,request) 
  result['nav'] = 'business'

  return render(request, 'scrap/home.html', result)
