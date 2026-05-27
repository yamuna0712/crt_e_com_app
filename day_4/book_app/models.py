from django.db import models

# Create your models here.

class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    quantity = models.IntegerField()
    publish_date = models.DateField()
class UserModel(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()