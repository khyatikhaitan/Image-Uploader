from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        labels={'photo':''}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap class to the 'photo' field
        self.fields['photo'].widget.attrs.update({'class': 'form-control'})