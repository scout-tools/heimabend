# serializers.py
import timeit
from rest_framework import serializers
from .models import Tag, Event, Message, Like, TagCategory
from django.db.models import Sum, Count
from django.core.cache import cache
from django.views.decorators.cache import cache_control


class TagSerializer(serializers.HyperlinkedModelSerializer):
    tag_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'tag_count',
            'description',
            'color',
            'category_id',
            'is_visible')

    def get_tag_count(self, obj):
        tag_id = 'tag_' + str(obj.id)
        tag_count = cache.get(tag_id)
        if tag_count is None:
            tag_count = Event.objects.filter(tags__id=obj.id).distinct().count()
            cache.set(tag_id, tag_count, timeout=24 * 60 * 60)
        return tag_count


class TagCategorySerializer(serializers.HyperlinkedModelSerializer):
    # tag_category_count = serializers.SerializerMethodField()

    class Meta:
        model = TagCategory
        fields = (
            'id',
            'name',
            'description',
            'ordered_id',
            # 'tag_category_count',
            'is_visible',
            'is_header',
        )

    """def get_tag_category_count(self, obj):
        print(obj)
        tag_id = 'tag_category' + str(obj.id)
        tag_count = cache.get(tag_id)
        if tag_count is None:
            tag_count = Tag.objects.filter(category_id=obj.id).distinct().count()
            cache.set(tag_id, tag_count, timeout=24 * 60 * 60)
        return tag_count"""


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
        # return getmedian()
        return 0


def getmedian():
    median = cache.get('median')
    if median is None:
        query = Like.objects.values("eventId__id").annotate(sum=Sum('opinionTypeId')).order_by('sum')
        median = query[int(query.count() / 2)]['sum']
        cache.set('median', median, timeout=12 * 60 * 60)
    return median


class EventSerializer(serializers.HyperlinkedModelSerializer):
    # like_score = serializers.SerializerMethodField()

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

    """def get_like_score(self, obj):
        # median = getmedian()
        score_id = 'like_score_' + str(obj.id)
        likescore = cache.get(score_id)
        if likescore is None:
            query = Like.objects.filter(eventId=obj.id).all().aggregate(sum=Sum('opinionTypeId'))
            likes = query['sum']

            if likes is None:
                likes = 0

            if likes < 3:
                likescore = 0
            elif likes < 10:
                likescore = 1
            elif likes < 20:
                likescore = 2
            elif likes == 30:
                likescore = 3
            else:
                likescore = 0
            cache.set(score_id, likescore, timeout=13 * 60 * 60)
        return likescore"""


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


class HighscoreSerializer(serializers.HyperlinkedModelSerializer):
    highscore = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'createdBy',
            'highscore',
        )

    def get_highscore(self, obj):
        score = Event.objects.filter(createdBy=obj['createdBy']).count()
        return score
