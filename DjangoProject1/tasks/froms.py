from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'image', 'status']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.content_type in ['image/jpeg', 'image/png', 'image/gif']:
                raise forms.ValidationError("JPG, PNG, GIF files are allowed")
            if image.size > 5*1024*1024:
                raise forms.ValidationError("imag size must be under 5MB")
        return image
