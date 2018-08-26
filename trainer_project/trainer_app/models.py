from django.db import models

class User(models.Model):
    MAN = 0
    WOMAN = 1

    name = models.CharField(max_length=128)
    email = models.EmailField()
    gender = models.IntegerField(editable=False)
    
