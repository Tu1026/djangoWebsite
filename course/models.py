from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	seatType_choices = [
		("general", "General Seats"),
		("restricted", "Restriced Seats"),
		("either", "Either")
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	url = models.URLField(verbose_name="URL of the desired course", max_length=200)
	name = models.CharField(verbose_name="What is the course code?", max_length=10)
	seatType = models.CharField(max_length=20, default="either", choices=seatType_choices)

	def __str__(self) -> str:
		return self.url
