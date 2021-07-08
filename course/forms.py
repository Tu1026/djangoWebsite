from django.forms import ModelForm
from .models import Course
from .task import course_reg_task

class CourseRegForm(ModelForm):
	class Meta:
		model= Course
		exclude=['user']
  
	def course_reg(self, course, email, url, number):
        # try to trick spammers by checking whether the honeypot field is
        # filled in; not super complicated/effective but it works
		print(course, email, url, number)
		id = course_reg_task.delay(
      	course, email, url, number)
		print(id.task_id)