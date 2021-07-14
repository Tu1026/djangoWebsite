from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CourseRegForm
from django.contrib.auth.decorators import login_required

@login_required
def course(request):
	if request.method == 'POST':
		form = CourseRegForm(request.POST)
		if form.is_valid():
			course = form.save(commit=False)
			course.user = request.user
			print(request.user.profile.discord_id)
			course.save()
			form.course_reg(form.cleaned_data.get("name"), request.user.email,form.cleaned_data.get("url"),
                   form.cleaned_data.get("seatType"), request.user.profile.discord_id)
			messages.success(request, 'Course has been added and we will beging tracking!')
			return redirect("main-home")
	else:
		form = CourseRegForm()
	return render(request, 'course/newCourse.html', {'form':form})

