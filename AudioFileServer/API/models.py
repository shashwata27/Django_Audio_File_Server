from django.db import models
from django_mysql.models import ListCharField
from datetime import datetime


# Create your models here.
class Song(models.Model):
    ID          =models.PositiveBigIntegerField(primary_key=True,null=False,blank=False,)
    Name        =models.CharField(max_length=100,null=False,blank=False,)#max_length=required
    Duration    =models.PositiveIntegerField(null=False,blank=False,)#blank is for who the fields are rendered
    UploadTime  =models.DateTimeField(default=datetime.now(),)#null are for database

class Podcast(models.Model):
    ID          =models.PositiveBigIntegerField(primary_key=True,null=False,blank=False,)
    Name        =models.CharField(max_length=100,null=False,blank=False,)
    Duration    =models.PositiveIntegerField(null=False,blank=False,)#starts from 0
    UploadTime  =models.DateTimeField(default=datetime.now(),)
    Host        =models.CharField(max_length=100,null=False,blank=False,)
    Participants=ListCharField(base_field=models.CharField(max_length=100),size=10,max_length=(10 * 101),null=True,blank=True ) # 10 * 100 character nominals, plus commas

class Audiobook(models.Model):
    ID          =models.PositiveBigIntegerField(primary_key=True,null=False,blank=False,)
    Title       =models.CharField(max_length=100,null=False,blank=False,)
    Author      =models.CharField(max_length=100,null=False,blank=False,)
    Narrator    =models.CharField(max_length=100,null=False,blank=False,)
    Duration    =models.PositiveIntegerField(null=False,blank=False,)
    UploadTime  =models.DateTimeField(default=datetime.now(),)