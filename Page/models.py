from django.db import models
# Create your models here.

class ContactUs(models.Model):
    FristName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField()
    Subject=models.CharField(max_length=200)
    Massage=models.TextField()
    def __str__(self):
        return self.Subject