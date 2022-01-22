from django.shortcuts import render, redirect
from django.contrib import messages

from gym.models import Gym
from .forms import GymRegForm
from django.contrib.auth.decorators import login_required

@login_required
def gym(request):
	if request.method == 'POST':
		form = GymRegForm(request.POST)
		if form.is_valid():
			gym = form.save(commit=False)
			gym.user = request.user
			print(request.user.profile.discord_id)
			gym.save()
			form.gym_reg(form.cleaned_data.get("name"),form.cleaned_data.get("url"),
                        request.user.profile.discord_id)
			messages.success(request, 'Gym session has been added and we will beging tracking!')
			return redirect("main-home")
	else:
		form = GymRegForm()
	return render(request, 'gym/newGym.html', {'form':form})

