# serializers.py
from rest_framework import serializers
from .models import Tag, Event, Message, Like, TagCategory, Image, Material, \
    ExperimentItem, Experiment
from rest_framework.serializers import Serializer, FileField
from django.core.cache import cache
from django.db.models import Sum


class TagSerializer(serializers.ModelSerializer):
    tag_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'tag_count',
            'description',
            'color',
            'category',
            'is_visible',
            'ordered_id'
        )

    def get_tag_count(self, obj):
        tag_id = 'tag_' + str(obj.id)
        tag_count = cache.get(tag_id)
        if tag_count is None:
            tag_count = Event.objects.filter(
                tags__id=obj.id).distinct().count()
            cache.set(tag_id, tag_count, timeout=24 * 60 * 60)
        return tag_count


class TagCategorySerializer(serializers.ModelSerializer):
    tag_category_count = serializers.SerializerMethodField()

    class Meta:
        model = TagCategory
        fields = (
            'id',
            'name',
            'description',
            'ordered_id',
            'tag_category_count',
            'is_visible',
            'is_header',
            'is_mandatory',
            'is_event_overview'
        )

    def get_tag_category_count(self, obj):
        tag_id = 'tag_category' + str(obj.id)
        tag_count = cache.get(tag_id)
        if tag_count is None:
            tag_count = Tag.objects.filter(
                category_id=obj.id).distinct().count()
            cache.set(tag_id, tag_count, timeout=24 * 60 * 60)
        return tag_count


class LikeSerializer(serializers.ModelSerializer):
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
        query = Like.objects.values("eventId__id").annotate(
            sum=Sum('opinionTypeId')).order_by('sum')
        median = query[int(query.count() / 2)]['sum']
        cache.set('median', median, timeout=12 * 60 * 60)
    return median


class EventSerializer(serializers.ModelSerializer):

    material_list = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Material.objects.all(),
        slug_field='name'
    )

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
            'material_list',
            'imageLink',
            'costsRating',
            'executionTimeRating',
            'isPrepairationNeeded',
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
            'isActive',
            'like_score')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'name',
            'email',
            'topic',
            'messageBody',
            'createdAt')


class HighscoreSerializer(serializers.ModelSerializer):
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


class StatisticSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    score_cumulative = serializers.SerializerMethodField()
    week = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'score',
            'score_cumulative',
            'week',
            'year'
        )

    def get_score(self, obj):
        score = Event.objects.filter(
            createdAt__year__exact=obj['year'],
            createdAt__week__exact=obj['week']).count()
        return score

    def get_score_cumulative(self, obj):
        score = Event.objects.filter(
            createdAt__year__lte=obj['year'],
            createdAt__week__lte=obj['week']).count()
        return score

    def get_week(self, obj):
        return obj['week']

    def get_year(self, obj):
        return obj['year']


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image', 'description', 'uploaded_at')


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = ('id', 'name', 'description')


class ExperimentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experiment
        fields = '__all__'


class ExperimentItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExperimentItem
        fields = '__all__'
