from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.clickjacking import xframe_options_exempt

from .forms import FileUpload
from .models import file_upload


# Create your views here.
def index(request):
    if request.method == "POST":
        c_form = FileUpload(request.POST, request.FILES)

        if c_form.is_valid():
            name = c_form.cleaned_data["File_name"]
            files = c_form.cleaned_data["files"]

            file_upload(file_name=name, myFile=files).save()

            rt = "<div> < a href = 'download/' > to download < / a >< a href = '' > to home < / a > < span > save success ! < / span > < / div > "
            return HttpResponse(rt)

        else:
            return HttpResponse("error occurred")

    else:
        context = {"form": FileUpload()}
        return render(request, "upload/fileUpload.html", context)


def show_down(request):
    data = file_upload.objects.all()
    context = {"data": data}
    return render(request, "upload/showFile.html", context)


class ListModelView(TemplateView):
    template_name = 'model3d/list.html'

    def get(self, request, **kwargs):
        list_file_uploads = file_upload.objects.all()

        context = {
            "list_file_uploads": list_file_uploads
        }
        return render(request, self.template_name, context=context)


class DetailModelView(TemplateView):
    template_name = 'model3d/detail.html'

    @xframe_options_exempt
    def get(self, request, pk, **kwargs):
        file = file_upload.objects.filter(pk=pk).first()
        # check ext
        if not file:
            return HttpResponse('nothing')
        ext_granted = ['glb', 'gltf']
        ext_file = file.myFile.url.split('.')[-1]
        if ext_file not in ext_granted:
            return HttpResponse('extension not found')
        context = {
            "url_file": file.myFile.url
        }
        return render(request, self.template_name, context=context)


class GetIdFileAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        files = file_upload.objects.all()
        # check ext
        if not files:
            return Response({'error': "nothing"},status=400)
        
        ext_granted = ['glb', 'gltf']
        for item in files:
            ext_file = item.myFile.url.split('.')[-1]
            if ext_file in ext_granted:
                return Response(item.ids)
        
        return Response({'error': "nothing"},status=400)
