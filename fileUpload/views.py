from django.shortcuts import render
from django.http import HttpResponse

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
