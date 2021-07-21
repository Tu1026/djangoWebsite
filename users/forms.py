from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from captcha.fields import CaptchaField
from .discord_check import main as check_valid_name
from django.core.exceptions import ValidationError
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

class UserRegisterationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model= Profile
		exclude=['user', 'image', "captcha"]
  
	def clean_discord_id(self):
		cleaned_data = self.clean()
		discord_name = cleaned_data.get('discord_id')
		name_list = discord_name.strip().split("#")
		if len(name_list) != 2:
			raise ValidationError("Please enter the format name#1234")
		print(name_list)
		state = False
		id = 0
		with ProcessPoolExecutor(max_workers=1) as executor:
			future = executor.submit(check_valid_name, name_list[0], name_list[1])
			state, id = future.result()
			print(f'future result {state} {id}')
		if not state: 
			raise ValidationError("Your discord name is not in the channel, have you joined the channel yet?")
		return id

class ProfileUpdate(forms.ModelForm):
	class Meta:
		model= Profile
		fields = ['discord_id']
  	
	def clean_discord_id(self):
		cleaned_data = self.clean()
		discord_name = cleaned_data.get('discord_id')
		name_list = discord_name.strip().split("#")
		if len(name_list) != 2:
			raise ValidationError("Please enter the format name#1234")
		print(name_list)
		state = False
		id = 0
		with ProcessPoolExecutor(max_workers=1) as executor:
			future = executor.submit(check_valid_name, name_list[0], name_list[1])
			state, id = future.result()
			print(f'future result {state} {id}')
		if not state:  # You create this function
			raise ValidationError("Your discord name is not in the channel, have you joined the channel yet?")
		return id
        
class UserUpdate(forms.ModelForm):
    class Meta:
        model= User
        fields = ['username', 'email']
    