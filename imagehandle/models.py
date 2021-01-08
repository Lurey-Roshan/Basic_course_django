from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=255)
	roll_no=models.IntegerField()
	image=models.ImageField(upload_to='student/')


	def __str__(self):
		return self.name