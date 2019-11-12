from django.db import models


# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    phone_number = models.CharField(max_length=16)
    date_employed= models.DateField()
    proffesion = models.CharField(max_length=20)


    def __str__(self):
        return self.first_name + '' + self.last_name 


    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    
   





