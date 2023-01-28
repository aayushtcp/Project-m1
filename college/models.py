from django.db import models

# Create your models here.
class Admission(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dob = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length= 14)
    grade = models.CharField(max_length= 13)
    address = models.CharField(max_length=255)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Admission form from ' + self.name + ' -- ' + self.email + ' -- ' + self.dob +' -- ' + self.grade

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length= 14)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' -- ' + self.email