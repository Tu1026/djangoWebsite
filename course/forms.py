from django.forms import ModelForm
from .models import Course

class CourseRegForm(ModelForm):
	class Meta:
		model= Course
		exclude=['user']