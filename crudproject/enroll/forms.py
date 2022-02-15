from django import forms
from django.db import models
from django.core import validators
from django.forms import fields, widgets
from .models import User
 

class StudentResistration(forms.ModelForm):
    class Meta:
       model = User
       fields = ['name','email','password']
       widgets ={
           'name': forms.TextInput(attrs={'class':'form-control'}),
           'email': forms.EmailInput(attrs={'class':'form-control'}),
           'password': forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
                  }
       
