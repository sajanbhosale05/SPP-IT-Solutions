from django.db import models
# Create your models here.
class Contact(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField(max_length=200)


    def __str__(self):
        return  self.name

class Application(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    role=models.CharField(max_length=200)
    experience=models.CharField(max_length=100)
    details=models.TextField(max_length=500)
    resume=models.FileField(blank=True,upload_to="media")

    def __str__(self):
        return self.role

