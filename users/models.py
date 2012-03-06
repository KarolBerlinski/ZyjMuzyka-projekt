from django.db import models

class User(models.Model):
	USER_TYPES =(
		('guest','GUEST'),
		('client','CLIENT'),
		('author','AUTHOR'),
		('premium','PREMIUM'),
		('admin','ADMIN'),
	)	
	
	nazwa=models.CharField(max_length=20)
	password=models.CharField(max_length=10)
	email=models.EmailField(max_length=75)
	typ=models.CharField(max_length=10,choices=USER_TYPES)

