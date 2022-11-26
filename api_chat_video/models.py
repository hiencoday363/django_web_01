from django.db import models

# Create your models here.
class UploadImageApi(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    myFile = models.FileField(upload_to="api/")

    def __str__(self):
        return self.file_name