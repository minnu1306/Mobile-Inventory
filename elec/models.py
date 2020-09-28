from django.db import models

# Create your models here.
class Company(models.Model):
	name=models.CharField(max_length=100)
	hq=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
	
class Mobile(models.Model):
	cId= models.ForeignKey(Company, on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	price=models.IntegerField()
	status=models.CharField(max_length=100,choices=[('available','available'),('sold out','sold out')])
	
	def __str__(self):
	 	return self.name
	
	
