from django.db import models
from band.models import Band
from users.model import User

class News(models.Model):

data=models.DateTimeField(auto_now=True,auto_add_now=True)
autor=models.ForeignKey(User)
temat=models.ForeignKey(Band,blank=True)
tresc=models.TextField()




