# serializers.py
from rest_framework import serializers
from .models import Tag, Event, Message, Like, TagCategory, Image, MaterialItem, \
    ExperimentItem, Experiment, MaterialUnit, MaterialName, MessageType, \
    Faq, FaqRating
from rest_framework_tracking.models import APIRequestLog
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
            'icon',
            'category',
            'is_visible',
            'sorting'
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
            'sorting',
            'icon',
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
            'event',
            'opinion_type_id',
            'like_created',
            'current_median'
        )

    def get_current_median(self, obj):
        # return getmedian()
        return 0


def getmedian():
    median = cache.get('median')
    if median is None:
        query = Like.objects.values("event__id").annotate(
            sum=Sum('opinion_type_id')).order_by('sum')
        median = query[int(query.count() / 2)]['sum']
        cache.set('median', median, timeout=12 * 60 * 60)
    return median


class EventSerializer(serializers.ModelSerializer):

    view_count = serializers.SerializerMethodField()
    header_image = serializers.SerializerMethodField()

    material_items = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=MaterialItem.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'tags',
            'material_items',
            'header_image',
            'costs_rating',
            'execution_time',
            'prepairation_time',
            'created_by',
            'created_by_email',
            'updated_by',
            'created_at',
            'updated_at',
            'is_active',
            'like_score',
            'view_count')

    def get_view_count(self, obj):
        return APIRequestLog.objects.filter(
            path='/basic/event/{}/'.format(obj.id)
        ).count()

    def get_header_image(self, obj):
        if obj.header_image:
            image_obj = Image.objects.filter(id=obj.header_image.id).first()
            image_str = image_obj.image.name
            image_field = image_str.split("/")[1]
            image_id = image_field.split(".")[0]
            return image_id

        return None


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class HighscoreSerializer(serializers.ModelSerializer):
    highscore = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'created_by',
            'highscore',
        )

    def get_highscore(self, obj):
        print(obj)
        score = Event.objects.filter(created_by=obj['created_by']).count()
        return score


class StatisticSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    score_cumulative = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'score',
            'score_cumulative',
            'month',
            'year'
        )

    def get_score(self, obj):
        score = Event.objects.filter(
            created_at__year__exact=obj['year'],
            created_at__month__exact=obj['month']).count()
        return score

    def get_score_cumulative(self, obj):
        score = Event.objects.filter(
            created_at__year__lte=obj['year'],
            created_at__month__lte=obj['month']).count()
        return score

    def get_month(self, obj):
        return obj['month']

    def get_year(self, obj):
        return obj['year']


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class MaterialItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialItem
        fields = '__all__'


class ExperimentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experiment
        fields = '__all__'


class ExperimentItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExperimentItem
        fields = '__all__'


class ExperimentOverviewSerializer(serializers.ModelSerializer):
    event_counter = serializers.SerializerMethodField()
    experiment_item = serializers.SerializerMethodField()

    class Meta:
        model = Experiment
        fields = (
            'id',
            'created_at',
            'age_level',
            'group_type',
            'group_leader',
            'event_counter',
            'experiment_item',
        )

    def get_event_counter(self, obj):
        return ExperimentItem.objects.filter(experiment__id=obj.id).count()

    def get_experiment_item(self, obj):
        return ExperimentItem.objects.filter(experiment__id=obj.id).values('score', 'event__title')


class TopViewsSerializer(serializers.ModelSerializer):

    view_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('id', 'view_count', 'title', 'created_by', 'header_image')

    def get_view_count(self, obj):
        return APIRequestLog.objects.filter(
            path='/basic/event/{}/'.format(obj.id)
        ).count()


class EventAdminSerializer(serializers.ModelSerializer):

    view_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'tags',
            'header_image',
            'created_by',
            'created_by_email',
            'updated_by',
            'created_at',
            'updated_at',
            'is_active',
            'like_score',
            'view_count')

    def get_view_count(self, obj):
        return APIRequestLog.objects.filter(
            path='/basic/event/{}/'.format(obj.id)
        ).count()


class EventTimestampSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id',
            'created_at')


class MaterialItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialItem
        fields = '__all__'


class MaterialUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialUnit
        fields = '__all__'


class MaterialNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialName
        fields = '__all__'


class MessageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageType
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = '__all__'


class FaqRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaqRating
        fields = '__all__'
