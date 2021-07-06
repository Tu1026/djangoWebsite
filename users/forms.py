from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields
from .models import Profile

class UserRegisterationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(ModelForm):
	class Meta:
		model= Profile
		exclude=['user', 'image']
