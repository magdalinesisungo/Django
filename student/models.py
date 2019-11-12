from django.db import models
from course.models import Course

import datetime


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
    courses = models.ManyToManyField(Course, blank=True, related_name= "students")

    def __str__(self):
        return self.first_name + '' + self.last_name 

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


    def calculate_age(self):
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month,today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    age = property(calculate_age)
        
    def clean(self):
        age = self.age
        if age < 17 or age > 30:
            raise ValidationError("For you to register in the platform you need to be above 17years and below 30years to register")

        return age

