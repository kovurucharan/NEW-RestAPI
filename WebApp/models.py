from django.db import models

# Create your models here.
class Employees(models.Model):
    EmpId=models.IntegerField()
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)

    def __str__(self):
        return self.FirstName