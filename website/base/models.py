from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Video(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	src = models.URLField(max_length=250)
	view_count = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.src

	@property
	def like_count(self):
		like_count = MetaData.objects.filter(video_id=self.id, is_liked=True).count()
		return like_count	

	@property
	def dislike_count(self):
		dislike_count = MetaData.objects.filter(video_id=self.id, is_disliked=True).count()
		return dislike_count

class MetaData(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	video = models.ForeignKey(Video, on_delete=models.CASCADE)
	is_liked = models.BooleanField(default=False)
	is_disliked = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username