from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignupForm(UserCreationForm):
	class Meta:
		model= User
		fields=['username', 'first_name','last_name','email', 'password1', 'password2']

class UpdateUser(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name']

class UpdateProfile(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=['address','contactno','profile_pic']

		widgets={
			'address':forms.TextInput(),
			'contactno':forms.TextInput(),
			'profile_pic':forms.FileInput(),
		}