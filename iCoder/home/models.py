from django.db import models

# Create your models here.

class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name = models.CharField(max_length  = 900)
    email = models.CharField(max_length  = 15)
    phone = models.CharField(max_length  = 900)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "message from: " +self.name

class  HomeBlog(models.Model):
    title = models.CharField(max_length=100)
    content=models.CharField(max_length = 10000)
    author = models.CharField(max_length= 100)

    def __str__(self):
        return self.title+ "  by "+ self.author