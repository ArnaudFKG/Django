from django.db import models

# Create your models here.

class Transaction(models.Model):
	date = models.DateTimeField("Date")
	source = models.CharField("From", max_length=64 , default="", blank=True)
	hashCode = models.CharField("Hash", max_length=64 , default="", blank=True)
	destination = models.CharField("To", max_length=64 , default="", blank=True)
	
	
	def __str__(self):
		return self.hashCode
	
	
	
	
	
