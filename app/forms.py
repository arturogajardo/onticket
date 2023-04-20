from django.forms import ModelForm
from .models import Event
from django import forms

class EventForm(ModelForm):
    title = forms.TextInput()
    description = forms.TextInput()
    image = forms.ImageField()
    url = forms.URLField()
    date = forms.DateField()
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'url', 'date']
        


