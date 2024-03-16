from django import forms
from .models import contactEnquiry,Post
from django.forms import ModelForm, TextInput, EmailInput
 

class contactForm(forms.ModelForm):
       class Meta:
        model = contactEnquiry
        fields = ("name", "email", "subject","message")
        widgets = {
            'name':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Roll'
                }),

            'phone':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'phone'
                }),

            'websiteLink':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'phone'
                }),
            
            
            'message':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'phone'
                })


            
        }




