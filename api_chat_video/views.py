from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from json import loads
import json

# Create your views here.
account = [
    {
        'username': 'admin',
        'password': 'admin'
    },
    {
        'username': 'user1',
        'password': 'user1'
    },
    {
        'username': 'user2',
        'password': 'user2'
    },
]


@csrf_exempt
def checkLogin(request):
    if request.method == 'GET':
        return HttpResponse('helloooo')
    elif request.method == 'POST':
        formData = loads(request.body)

        try:
            username = formData['username']
            password = formData['password']
        except:
            return HttpResponse('invalid form', status=400, statusText='invalid form')

        for user in account:

            if user['username'] == username:
                if user['password'] == password:
                    return HttpResponse('active', status=200)
                else:
                    return HttpResponse('the incorrect password', status=401)

        return HttpResponse('the account do not exist', status=403)

    else:
        return HttpResponse('helloooo')


@csrf_exempt
def getFullAcc(request):
    if request.method == 'POST':
        username = loads(request.body)['username']
        listAcc = [item for item in account if item['username'] != username]
        return HttpResponse(json.dumps(listAcc), content_type='application/json', status=200)
    else:
        return HttpResponse('nothing', status=400)
