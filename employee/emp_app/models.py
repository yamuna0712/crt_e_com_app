from django.db import models

# Create your models here.
class Emp_data(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=255)
    emp_email=models.EmailField(max_length=55)
    emp_salary=models.IntegerField()
    emp_phone=models.IntegerField()
    emp_address=models.TextField()
    emp_joindate=models.DateField()
    emp_gender=models.CharField(max_length=10)
    emp_age=models.IntegerField()
    emp_dept=models.CharField(max_length=30)
    emp_experience=models.IntegerField()

