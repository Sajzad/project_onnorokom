from django.db import models

# Create your models here.


class Video(models.Model):
	src = models.URLField(max_length=250)

	def __str__(self):
		return self.src