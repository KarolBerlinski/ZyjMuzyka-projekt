from django.db import models
from band.models import Band

class Wystep(models.Model):
	data_wystepu = models.DateField(auto_now=False, auto_now_add=False)
	band = models.ForeignKey(Band)
	miasto=models.CharField(max_length=100)
	adres=models.CharField(max_length=200)
	ilosc_miejsc=models.IntegerField();
	cena_za_miejsce=models.DecimalField(max_digits=6,decimal_places=2)
	
