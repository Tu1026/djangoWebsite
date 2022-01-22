from django.db import models
from django.contrib.auth.models import User

class Gym(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	url = models.URLField(verbose_name="URL of the desired 'section' of the the gym session", max_length=200)
	name = models.CharField(verbose_name="What is the the time of the session? (So you can know)", max_length=10)

	def __str__(self) -> str:
		return self.url
