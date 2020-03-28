# serializers.py
import timeit
from rest_framework import serializers
from .models import Tag, Event, Message, Like


class TagSerializer(serializers.HyperlinkedModelSerializer):
    tag_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'tag_count',
            'description',
            'color')

    def get_tag_count(self, obj):
        return Event.objects.filter(tags__name__contains=obj).distinct().count()


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = (
            'eventId',
            'opinionTypeId',
            'like_created'
        )


class EventSerializer(serializers.HyperlinkedModelSerializer):
    like_score = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'isPossibleOutside',
            'isPossibleInside',
            'tags',
            'material',
            'costsRating',
            'executionTimeRating',
            'isPrepairationNeeded',
            'isActive',
            'isLvlOne',
            'isLvlTwo',
            'isLvlThree',
            'isPossibleDigital',
            'isPossibleAlone',
            'createdBy',
            'createdByEmail',
            'updatedBy',
            'createdAt',
            'updatedAt',
            'like_score')

    def get_like_score(self, obj):
        return 3


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'name',
            'email',
            'topic',
            'messageBody',
            'createdAt')
