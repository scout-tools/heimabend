# models.py
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator 


class Tag(models.Model):
    id = models.AutoField( 
            auto_created = True, 
            primary_key = True, 
            serialize = False,  
            verbose_name ='ID')
    name = models.CharField(max_length=60)
    beschreibung = models.CharField(max_length=60)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField( 
            auto_created = True, 
            primary_key = True, 
            serialize = False,  
            verbose_name ='ID')
    title = models.CharField(max_length=60)
    beschreibung = models.CharField(max_length=60)
    isPossibleOutside = models.BooleanField(default=1)
    isPossibleInside = models.BooleanField(default=1)
    tags = models.ManyToManyField(Tag, default='')
    createdAt = models.DateTimeField(default=now, editable=False)
    material = models.CharField(max_length=60, default='')
    costsRating = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])
    prepairationRating = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])



    def __str__(self):
        return self.title
