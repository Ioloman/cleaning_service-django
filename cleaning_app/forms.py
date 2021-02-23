from .models import Service
from django.forms import ModelForm


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'price']
