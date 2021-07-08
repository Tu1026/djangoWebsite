from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm, UserProfileForm, UserUpdate, ProfileUpdate
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterationForm(request.POST)
		profile_form = UserProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user = form.save()
			profile_instance = profile_form.save(commit=False)
			profile_instance.user = user
			profile_instance.save()
			messages.success(request, 'Account has been created! You can log in here')
			return redirect("login")
	else:
		form = UserRegisterationForm()
		profile_form = UserProfileForm()
	return render(request, 'users/register.html', {'form':form, 'profile': profile_form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdate(request.POST, instance=request.user)
		p_form = ProfileUpdate(request.POST, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'{u_form.cleaned_data.get("username")}, your account has been updated!')
			return redirect("profile")
	else: 
		u_form = UserUpdate(instance=request.user)
		p_form = ProfileUpdate(instance=request.user.profile)
    
	context = {
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request, 'users/profile.html', context)
