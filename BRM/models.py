from django.db import models
from django.contrib.auth.models import User

class BRMuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.user.username
    

class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    author=models.CharField(max_length=110)
    publisher=models.CharField(max_length=220,help_text="Please enter publisher detalis")
    def __str__(self):
        return self.title
    class Meta:
        ordering=['title']
    objects=models.Manager
