# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator


class Tag(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    title = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(40)])
    description = models.CharField(
        max_length=2000,
        default='',
        validators=[
            MinLengthValidator(75),
            MaxLengthValidator(2000)])
    isPossibleOutside = models.BooleanField(default=1)
    isPossibleInside = models.BooleanField(default=1)
    tags = models.ManyToManyField(Tag, default='')
    material = models.CharField(max_length=200, default='', blank=True)
    costsRating = models.SmallIntegerField(
        default=1, validators=[
            MinValueValidator(0), MaxValueValidator(3)])
    executionTimeRating = models.SmallIntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(3)])
    isPrepairationNeeded = models.BooleanField(default=1)
    isActive = models.BooleanField(default=0)
    isLvlOne = models.BooleanField(default=1)
    isLvlTwo = models.BooleanField(default=0)
    isPossibleDigital = models.BooleanField(default=0)
    isPossibleAlone = models.BooleanField(default=0)
    isLvlThree = models.BooleanField(default=0)
    createdBy = models.CharField(max_length=60, blank=True)
    createdByEmail = models.CharField(max_length=60, blank=True)
    updatedBy = models.CharField(max_length=60, null=True, blank=True)
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    topic = models.CharField(max_length=40)
    messageBody = models.CharField(max_length=1000)
    createdAt = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name