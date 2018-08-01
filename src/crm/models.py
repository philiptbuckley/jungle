from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
	content	= models.TextField()
	created_by	= models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse("notes:note-detail", kwargs={"id": self.id})