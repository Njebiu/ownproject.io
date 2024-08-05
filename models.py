from django.db import models

# Create your models here.

class StudentsModels(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class StudentDetailsModels(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=50, choices=[('M','Male'), ('F','Female'), ('O','Other')])

    class Meta:
        db_table = ('students')


