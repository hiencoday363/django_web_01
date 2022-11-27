from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from json import loads
import json
import base64
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UploadImageApi
from .serializers import UploadImageApiSerializer, UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetImageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        images = UploadImageApi.objects.all()
        serializer = UploadImageApiSerializer(images, many=True)
        return Response(serializer.data)


class UploadImageApiView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        serializer = UploadImageApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadImageDetail(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_obj(self, id):
        try:
            return UploadImageApi.objects.get(id=id)
        except UploadImageApi.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        image = self.get_obj(id)
        serializer = UploadImageApiSerializer(image)
        return JsonResponse(serializer.data)

    def put(self, request, id):
        image = self.get_obj(id)

        try:
            if request.data['myFile'].name == str(image.myFile).replace('api/', ""):
                del request.data['myFile']
        except:
            pass

        serializer = UploadImageApiSerializer(image, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        image = self.get_obj(id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
class UploadViewSet(viewsets.ModelViewSet):
    def list(self, request):
        uploadImages = UploadImageApi.objects.all()
        serializer = UploadImageApiSerializer(uploadImages, many=True)
        return JsonResponse(data=serializer.data, safe=False)

    def create(self, request, *args, **kwargs):
        fileName = request.data['file_name']
        myFile = request.data['myFile']
        UploadImageApi.objects.create(file_name=fileName, myFile=myFile)
        return JsonResponse({'message': 'created'}, status=201)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
'''

# @csrf_exempt
# def upload_serializer(request):
#     if request.method == 'GET':
#         uploadImages = UploadImageApi.objects.all()
#         serializer = UploadImageApiSerializer(uploadImages, many=True)
#         return JsonResponse(data=serializer.data, safe=False)
#
#     elif request.method == "POST":
#         print("request:", request)
#         data = JSONParser().parse(request)
#         serializer = UploadImageApiSerializer(data=data)
#         if serializer.is_valid():
#             print(serializer)
#             print('data:', serializer.data)
#             # serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#

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
    {
        'username': 'user3',
        'password': 'user3'
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

# @csrf_exempt
# def getFullAcc(request):
#     if request.method == 'POST':
#         username = loads(request.body)['username']
#         listAcc = [item for item in account if item['username'] != username]
#         return HttpResponse(json.dumps(listAcc), content_type='application/json', status=200)
#     else:
#         return HttpResponse('nothing', status=400)
