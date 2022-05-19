from django.db import models

# Create your models here.
class Blog(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.TextField()
    Date=models.DateTimeField()

    def __str__(self):
        return self.Title