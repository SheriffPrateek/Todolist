from django.db import models

# Create your models here.
class Notes(models.Model):
	title= models.TextField()
	description =models.TextField()