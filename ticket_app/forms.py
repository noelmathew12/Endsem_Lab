from django import forms
from .models import Post
from django.forms import ModelForm

class MymodelForm(ModelForm):    
    class meta:
        model = Post
        fields = ['cities']
