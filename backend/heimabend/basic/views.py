# views.py
import json

from django.db.models.functions import ExtractWeek, ExtractYear
from django.http import HttpResponse
from django_filters import FilterSet, BooleanFilter, OrderingFilter, \
    ModelMultipleChoiceFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets, mixins, generics, \
    filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Tag, Event, Message, Like, TagCategory, Image, \
     Material, ExperimentItem, Experiment
from .serializers import TagSerializer, EventSerializer, MessageSerializer, \
    LikeSerializer, HighscoreSerializer, \
    TagCategorySerializer, StatisticSerializer, ImageSerializer, \
    MaterialSerializer, ExperimentItemSerializer, ExperimentSerializer


class TagViewSet(LoggingMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all().order_by('ordered_id', 'name')
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('is_visible',)


class TagCategoryViewSet(LoggingMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = TagCategory.objects.all().order_by('ordered_id', 'name')
    serializer_class = TagCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('is_visible',)


class EventPagination(pagination.PageNumberPagination):
    page_size = 5  # the no. of company objects you want to send in one go


class EventFilter(FilterSet):
    isPossibleInside = BooleanFilter(field_name='isPossibleInside')
    isPossibleOutside = BooleanFilter(field_name='isPossibleOutside')
    isPossibleDigital = BooleanFilter(field_name='isPossibleDigital')
    isPossibleAlone = BooleanFilter(field_name='isPossibleAlone')
    isPrepairationNeeded = BooleanFilter(field_name='isPrepairationNeeded')
    isActive = BooleanFilter(field_name='isActive', method='get_isActive')
    withoutCosts = BooleanFilter(
        method='get_CostRating', field_name='costsRating')

    filterTags = ModelMultipleChoiceFilter(field_name='tags__id',
                                           to_field_name='id',
                                           queryset=Tag.objects.all(),
                                           method='get_tags')
    isLvlOne = BooleanFilter(field_name='isLvlOne')
    isLvlTwo = BooleanFilter(field_name='isLvlTwo')
    isLvlThree = BooleanFilter(field_name='isLvlThree')

    class Meta:
        model = Event
        fields = ['isPossibleInside',
                  'isPossibleOutside',
                  'isPossibleAlone',
                  'isPossibleDigital',
                  'isPrepairationNeeded',
                  'isActive',
                  'withoutCosts',
                  'filterTags',
                  'isLvlOne',
                  'isLvlTwo',
                  'isLvlThree'
                  ]

    def get_CostRating(self, queryset, field_name, value):
        if value:
            return queryset.filter(costsRating=0)
        return queryset

    def get_isActive(self, queryset, field_name, value):
        if not value:
            if self.request.user.is_authenticated:
                return queryset.filter(isActive=value)
        return queryset.filter(isActive=True)

    def get_tags(self, queryset, field_name, value):
        tags_category = dict()

        for val in value:
            tags_category.setdefault(str(val.category.id), []).append(val.id)

        for filter_elements in tags_category:
            queryset = queryset.filter(
                tags__id__in=tags_category[filter_elements]).distinct()

        return queryset


class EventViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    filterset_class = EventFilter
    ordering = ['-createdAt']
    ordering_fields = ['-createdAt', 'title', '-like_score']
    search_fields = ['title', 'description', 'material']
    pagination_class = EventPagination

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.queryset.filter(isActive=True)

    def create(self, request, *args, **kwargs):
        # Check whether new_item exists
        if 'material_list' in request.data:
            material_list = request.data['material_list']
            for new_item in material_list:
                if not Material.objects.filter(name__exact=new_item).exists():
                    new_material = Material.objects.create(name=new_item)
                    new_material.save()

        return super().create(request, *args, **kwargs)

    def update(self, request, pk=None, partial=False):
        if 'material_list' in request.data:
            material_list = request.data['material_list']
            for new_item in material_list:
                if not Material.objects.filter(name__exact=new_item).exists():
                    new_material = Material.objects.create(name=new_item)
                    new_material.save()

        return super().update(request, pk, partial=partial)


class MessageViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('createdAt')
    serializer_class = MessageSerializer


class LikeViewSet(LoggingMixin, mixins.CreateModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class HighscoreView(LoggingMixin, mixins.ListModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Event.objects.values('createdBy').distinct()
    serializer_class = HighscoreSerializer


class StatisticView(LoggingMixin, mixins.ListModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Event.objects.values(week=ExtractWeek('createdAt')).annotate(year=ExtractYear('createdAt')).values(
        'week', 'year').distinct().order_by('year', 'week')
    serializer_class = StatisticSerializer


class ImageView(LoggingMixin, viewsets.ModelViewSet, generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = ImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class MaterialViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class ExperimentViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer


class ExperimentItemViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = ExperimentItem.objects.all()
    serializer_class = ExperimentItemSerializer


class RandomEventViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.order_by("?")[:1]
    serializer_class = EventSerializer
