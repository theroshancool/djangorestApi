from django.db import models

# Create your models here.


class Departments(models.Model):
    objects = None
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=300)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateTimeField()
    PhotoFileName = models.CharField(max_length=500)