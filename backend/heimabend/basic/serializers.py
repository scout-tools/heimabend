# serializers.py
from rest_framework import serializers

from .models import Tag, Event


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'beschreibung', 'color')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'beschreibung',
            'isPossibleOutside',
            'isPossibleInside',
            'tags',
            'createdAt',
            'material',
            'costsRating',
            'prepairationRating')
