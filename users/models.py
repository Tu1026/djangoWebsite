from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
import random
random_dogs = os.listdir(settings.MEDIA_ROOT)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	discord_id=models.CharField(verbose_name="Discord_id (like this xxxx#1234)", max_length=50)
	image = models.ImageField(default=random.choice(random_dogs), upload_to="profile_pics")

	def __str__(self) -> str:
		return f'{self.user.username} Profile'

