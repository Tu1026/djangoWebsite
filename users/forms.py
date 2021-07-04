from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterationForm(UserCreationForm):
	email = forms.EmailField()
	discord_id = forms.CharField(label="Discord ID", max_length=50)

	class Meta:
		model = User
		fields = ['username', 'email', 'discord_id', 'password1', 'password2']