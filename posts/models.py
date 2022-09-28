from django.db import models

class Sport(models.Model):
	name = models.CharField(max_length=30)
	image = models.ImageField()

	def __str__(self):
		return "{}".format(self.name)

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField()
	sport_name = models.ForeignKey("Sport",null=True, on_delete=models.CASCADE)
	def __str__(self):
		return "{}".format(self.title)

class Comment(models.Model):
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	author = models.CharField(max_length=50)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "{} {}".format(self.author, self.date)
# Create your models here.
