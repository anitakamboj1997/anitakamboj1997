from django.core import validators
from django import forms

from .models import Student

class sturesgistration(forms.ModelForm):
    
  
    class Meta:
       model= Student
       fields = "__all__"
