from django.db import models
from band.models import Band

class Towar(models.Model)

TOWAR_WYBOR=(
	('plyta','Plyta')
	('koszulka','Koszulka')
	('kubek','Kubek')
	('chusta','Chusta')
	('zapalniczka','Zapalniczka')
	('piersiowka','Piersiowka')
)

nazwa_towaru=CharField(max_length=45)
band = models.ForeignKey(Band,blank=True)
typ_towaru=CharField(max_length=40,choices=TOWAR_WYBOR)

