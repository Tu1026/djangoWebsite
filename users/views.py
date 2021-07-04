from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, 'Account has been created! You can log in here')
			return redirect("login")
	else:
		form = UserRegisterationForm()
	return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
	return render(request, 'users/profile.html')
