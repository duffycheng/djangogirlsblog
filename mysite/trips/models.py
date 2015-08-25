from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.CharField(blank=True, max_length=100)
	location = models.CharField(max_length=100)
	create_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title