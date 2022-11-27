from django import forms


class FileUpload(forms.Form):
    File_name = forms.CharField(
        widget = forms.TextInput(attrs={"class": "form-control mt-3"})
        )
    files = forms.FileField(
        widget = forms.FileInput(attrs={"class": "form-control mt-3"})
        )
    
