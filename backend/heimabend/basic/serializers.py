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
        return 5


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
