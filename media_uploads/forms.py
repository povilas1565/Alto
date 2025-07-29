from django import forms
from .models import MediaFile

class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'caption', 'file', 'media_type', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'caption': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'media_type': forms.Select(attrs={'class': 'form-control'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }