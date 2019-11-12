from django.db import models
from teacher.models import Teacher



# Create your models here.


class Course(models.Model):
	name = models.CharField(max_length=50)
	date_started = models.CharField(max_length=50)
	end_date = models.CharField(max_length=50)
	duration_in_month = models.IntegerField()
	description = models.TextField()
	teacher = models.ForeignKey(Teacher,null=True, on_delete=models.CASCADE)


	def __str__(self):
		return self.name

	

