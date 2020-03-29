# serializers.py
import timeit
from rest_framework import serializers
from .models import Tag, Event, Message, Like
from django.db.models import Sum
from django.core.cache import cache


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
        return Event.objects.filter(tags__id=obj.id).distinct().count()


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    current_median = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = (
            'eventId',
            'opinionTypeId',
            'like_created',
            'current_median'
        )

    def get_current_median(self, obj):
        global median
        query = Like.objects.values("eventId__id").annotate(sum=Sum('opinionTypeId')).order_by('sum')
        median = query[int(query.count() / 2)]['sum']
        return median


median = 0


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
        global median
        score_id = 'like_score_' + str(obj.id)
        likescore = cache.get(score_id)
        if likescore is not None:
            return likescore
        else:
            query = Like.objects.filter(eventId=obj.id).all().aggregate(sum=Sum('opinionTypeId'))
            likes = query['sum']
            if likes is None:
                likes = 0
            border = median * 0.1
            if likes > median + border:
                cache.set(score_id, 3, timeout=20)
                return 3
            elif likes < median - border:
                cache.set(score_id, 1, timeout=20)
                return 1
            elif likes == 0:
                cache.set(score_id, 0, timeout=20)
                return 0
            else:
                cache.set(score_id, 2, timeout=20)
                return 2


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
