from django.db import models
from course.models import Course


# Create your models here.
class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=20)
	registration_number = models.CharField(max_length=20)
	email = models.EmailField(max_length=70)
	phone_number = models.CharField(max_length=16)
	date_joined = models.DateField()
	image = models.ImageField(upload_to="profile_image",blank=True)
	courses = models.ManyToManyField(Course)

	def __str__(self):
		return self.first_name + '' + self.last_name 

