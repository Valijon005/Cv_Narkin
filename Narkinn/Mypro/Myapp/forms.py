from django import forms
from .models import *

class Managmentforms(forms.ModelForm):
    class Meta:
        model = Managment
        fields = ['name', 'email', 'text', 'phone']


