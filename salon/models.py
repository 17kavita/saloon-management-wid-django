from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class UserSignup(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    contect=models.CharField(max_length=12)
    gender=models.CharField(max_length=12)
    image=models.FileField(null=True)

    def __str__(self):
        return self.fname
