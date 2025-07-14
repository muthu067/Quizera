from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ContactForm(forms.Form):
    name=forms.CharField(label='name',max_length=100,required=True)
    email=forms.CharField(label='email',required=True)
    message=forms.CharField(label='message',required=True)

class Register_Form(forms.ModelForm):
    username=forms.CharField(label='Username',required=True)
    email=forms.CharField(label='Email',required=True)
    password=forms.CharField(label='Password',required=True)
    confirm_password=forms.CharField(label='Confirm Password',required=True)

    class Meta:
        model=User
        fields=['username','email','password']
    
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        con_password=cleaned_data.get('confirm_password')

        if password and con_password and password!=con_password:
            raise forms.ValidationError("Passwords Do not Match")
        
class Login(forms.Form):
    username=forms.CharField(label='Username',required=True)
    password=forms.CharField(label='Password',required=True)

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')

        if username and password:
            user=authenticate(username=username,password=password)
            if user is None:
                raise forms.ValidationError("Invalid username")