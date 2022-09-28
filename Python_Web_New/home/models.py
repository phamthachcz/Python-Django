from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} {} {}".format(self.name, self.email, self.date)
# Create your models here.
