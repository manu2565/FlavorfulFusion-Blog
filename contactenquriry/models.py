from enum import auto
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()


class singlepost(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=50)
    message=models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default=timezone.now)
    
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
   
   

class Services(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_des=models.TextField()








class SubPlan(models.Model):
    title=models.CharField(max_length=150)
    price=models.IntegerField()
    highlight_status=models.BooleanField(default=False,null=True)


    def __str__(self):
        return self.title


#Subscription plane Features
    
class SubPlanFeature(models.Model):
    subplan=models.ForeignKey(SubPlan, on_delete=models.CASCADE)
    

    

    title=models.CharField(max_length=150)


    def __str__(self):
        return self.title


class Posts(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title