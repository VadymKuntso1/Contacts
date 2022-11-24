from django.db import models

class Contact(models.Model):
    id = models.IntegerField('id',primary_key=True, auto_created=True)
    photo = models.FileField('photo',upload_to='uploads/',null=True,blank=True)
    name = models.CharField('name', max_length=100)
    seccond_name = models.CharField('seccond_name', max_length=100)
    third_name = models.CharField('third_name', max_length=100)
    number = models.CharField('number', max_length=100)
