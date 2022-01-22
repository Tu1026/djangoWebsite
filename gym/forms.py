from django import forms
from django.forms import ModelForm
from .models import Gym
from .task import gym_reg_task

class GymRegForm(ModelForm):
	class Meta:
		model= Gym
		exclude=['user']
  
	def gym_reg(self, course, url, uid):
		print(course, url)
		id = gym_reg_task.delay(
      	course, url, uid)
		print(id.task_id)