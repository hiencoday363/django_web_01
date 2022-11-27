from django.contrib import admin

from .models import UploadImageApi

# Register your models here.
# admin.site.register(UploadImageApi)

# use the way 2: class
@admin.register(UploadImageApi)
class UploadImageApiModel(admin.ModelAdmin):
    list_filter = ('file_name', 'myFile')
    list_display = ('file_name', 'myFile')