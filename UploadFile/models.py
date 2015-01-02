from django.db import models
# Create your models here.

class Document(models.Model):
  course_name = models.CharField(max_length=100, null=True)
  course_code = models.CharField(max_length=24, null=False)
  category = models.CharField(max_length=24)
  year = models.IntegerField()
  prof = models.CharField(max_length=100, null=True)
  description = models.CharField(max_length=1000)
  docfile = models.FileField(upload_to='documents/%Y/%m/%d')