from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
	address=models.TextField(null=True, blank=True)
	contactno=models.IntegerField(null=True, blank=True)
	profile_pic=models.ImageField(blank=True, null=True, upload_to='profile/')
	
	def imageURL(self):
		try:
			url=self.profile_pic.url
		except:
			url=''
		return url
	