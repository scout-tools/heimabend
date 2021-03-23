# models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, \
    MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField, JPEGField
import uuid


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class TagCategory(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    ordered_id = models.IntegerField(blank=False, unique=True)
    is_visible = models.BooleanField(default=True)
    is_header = models.BooleanField(default=False)
    is_mandatory = models.BooleanField(default=False)
    is_event_overview = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Material(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Tag(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=7)
    category = models.ForeignKey(
        TagCategory, on_delete=models.PROTECT, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    ordered_id = models.IntegerField(blank=False, unique=False, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Event(TimeStampMixin):
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
        max_length=8000,
        default='',
        validators=[
            MinLengthValidator(75),
            MaxLengthValidator(8000)])
    isPossibleOutside = models.BooleanField(default=1)
    isPossibleInside = models.BooleanField(default=1)
    tags = models.ManyToManyField(Tag, default='')
    material = models.CharField(max_length=1000, default='', blank=True)
    material_list = models.ManyToManyField(Material, blank=True)
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
    imageLink = models.CharField(max_length=120, blank=True, null=True)
    createdBy = models.CharField(max_length=60, blank=True)
    createdByEmail = models.CharField(max_length=60, blank=True)
    updatedBy = models.CharField(max_length=60, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(null=True, blank=True)
    like_score = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()


class Message(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    topic = models.CharField(max_length=40)
    messageBody = models.CharField(max_length=1000)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Like(TimeStampMixin):
    class OptionType(models.IntegerChoices):
        LIKE = 1, _('Like'),
        DISLIKE = -1, _('Dislike'),

    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    opinionTypeId = models.IntegerField(
        choices=OptionType.choices, default=OptionType.LIKE)
    like_created = models.DateTimeField(auto_now_add=True, editable=False)

    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)
        if self.id:
            query = Like.objects.filter(eventId=self.eventId).all(
            ).aggregate(sum=Sum('opinionTypeId'))
            likes = query['sum']

            if likes is None:
                likes = 0

            if likes < 3:
                likescore = 0
            elif likes < 10:
                likescore = 1
            elif likes < 20:
                likescore = 2
            elif likes >= 20:
                likescore = 3
            else:
                likescore = 0

            event = Event.objects.filter(id=self.eventId.id).first()
            event.like_score = likescore
            event.save()


def nameFile(instance, filename):
    return 'images/' + str(uuid.uuid1()) + '.jpeg'


class Image(TimeStampMixin):
    image = StdImageField(upload_to=nameFile, blank=True, variations={
        'default': (600, 400),
    }, delete_orphans=True)
    description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.description, self.image)

    def __repr__(self):
        return self.__str__()


class Experiment(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    age_level = models.IntegerField(blank=False, unique=False, null=True)
    group_type = models.IntegerField(blank=False, unique=False, null=True)
    group_leader = models.IntegerField(blank=False, unique=False, null=True)

    def __str__(self):
        return '{} {} {} {}'.format(
            self.id,
            self.age_level,
            self.group_type,
            self.group_leader)

    def __repr__(self):
        return self.__str__()


class ExperimentItem(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    experiment_id = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    score = models.IntegerField(blank=False, unique=False, null=True)

    def __str__(self):
        return '{} {} {}'.format(
            self.event_id,
            self.experiment_id,
            self.score)

    def __repr__(self):
        return self.__str__()
