# serializers.py
from rest_framework import serializers

from .models import Tag, Event


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
        count_loop = 0
        for singleE in Event.objects.all():
            if obj in singleE.tags.all():
                count_loop += 1

        return count_loop


class LikeSerializer(serializers.HyperlinkedModelSerializers):

    def get_score(self, obj):
        return 3


class EventSerializer(serializers.HyperlinkedModelSerializer):
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
            'updatedAt')

# class TagSerializer(serializers.Serializer):
#     tag_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Tag
#         fields = (
#             'id',
#             'name',
#             'tag_count',
#             'description',
#             'sub',
#             'color')

#     def get_tag_count(self, obj):
#         entry_list = Event.objects.values('tags')
#         # print(entry_list)
#         print(obj.id)
#         return Event.objects.filter(isLvlOne=False).count()
