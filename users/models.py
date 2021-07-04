from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	discord_id=models.CharField(verbose_name="dicord_id", max_length=50)
	image = models.ImageField(default='default.jpg', upload_to="profile_pics")

	def __str__(self) -> str:
		return f'{self.user.username} Profile'
