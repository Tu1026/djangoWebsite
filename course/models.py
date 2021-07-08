from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	url = models.URLField(verbose_name="URL of the desired course", max_length=200)
	name = models.CharField(verbose_name="What is the course code?", max_length=10)
	seats = models.IntegerField(verbose_name="How many people are currently registered?")

	def __str__(self) -> str:
		return self.url
