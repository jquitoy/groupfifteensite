from django.db import models

# Create your models here.
 
class Genders(models.Model):
	gender_id = models.BigAutoField(primary_key=True, blank=False)
	gender = models.CharField(max_length=55, blank=False)
	