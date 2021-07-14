from django.shortcuts import render

def home(request):
	return render(request, 'main/home.html')

def tutorial(request):
    return render(request, 'main/tutorial.html')