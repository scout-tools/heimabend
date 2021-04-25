# views.py
import json

from django.db.models.functions import ExtractMonth, ExtractYear
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
from rest_framework.views import APIView

from .models import Tag, Event, Message, Like, TagCategory, Image, \
    MaterialItem, ExperimentItem, Experiment, MaterialUnit, \
    MaterialName, MessageType, Faq, FaqRating, NextBestHeimabend
from .serializers import TagSerializer, EventSerializer, MessageSerializer, \
    LikeSerializer, HighscoreSerializer, \
    TagCategorySerializer, StatisticSerializer, ImageSerializer, \
    MaterialItemSerializer, ExperimentItemSerializer, ExperimentSerializer, \
    TopViewsSerializer, EventAdminSerializer, EventTimestampSerializer, \
    MaterialUnitSerializer, MaterialNameSerializer, MessageTypeSerializer, \
    FaqSerializer, FaqRatingSerializer, ExperimentOverviewSerializer, \
    NextBestHeimabendSerializer


class TagViewSet(LoggingMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all().order_by('sorting', 'name')
    serializer_class = TagSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.queryset.filter(is_visible=True)
        else:
            return self.queryset

    def create(self, request, pk=None, partial=False):
        return super().create(request, pk, partial=partial)

    def update(self, request, pk=None, partial=False):
        return super().update(request, pk, partial=partial)


class TagCategoryViewSet(LoggingMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = TagCategory.objects.all().order_by('sorting', 'name')
    serializer_class = TagCategorySerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.queryset.filter(is_visible=True)
        else:
            return self.queryset

    def create(self, request, pk=None, partial=False):
        return super().create(request, pk, partial=partial)

    def update(self, request, pk=None, partial=False):
        return super().update(request, pk, partial=partial)


class EventPagination(pagination.PageNumberPagination):
    page_size = 5  # the no. of company objects you want to send in one go


class EventFilter(FilterSet):
    prepairation_time = BooleanFilter(field_name='prepairation_time')
    is_active = BooleanFilter(field_name='is_active', method='get_is_active')
    withoutCosts = BooleanFilter(
        method='get_cost_rating', field_name='costs_rating')
    filterTags = ModelMultipleChoiceFilter(field_name='tags__id',
                                           to_field_name='id',
                                           queryset=Tag.objects.all(),
                                           method='get_tags')

    class Meta:
        model = Event
        fields = ['prepairation_time',
                  'is_active',
                  'withoutCosts',
                  'filterTags',
                  ]

    def get_CostRating(self, queryset, field_name, value):
        if value:
            return queryset.filter(costs_rating=0)
        return queryset

    def get_is_active(self, queryset, field_name, value):
        if not value:
            if self.request.user.is_authenticated:
                return queryset.filter(is_active=value)
        return queryset.filter(is_active=True)

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
    ordering = ['-created_at']
    ordering_fields = ['-created_at', 'title', '-like_score']
    search_fields = ['title', 'description', 'material']
    pagination_class = EventPagination

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.queryset.filter(is_active=True)
        else:
            return self.queryset

    def create(self, request, *args, **kwargs):
        # Check whether new_item exists
        if 'material_items' in request.data:
            material_items = request.data['material_items']
            for new_item in material_items:
                if not Material.objects.filter(name__exact=new_item).exists():
                    new_material = Material.objects.create(name=new_item)
                    new_material.save()

        return super().create(request, *args, **kwargs)

    def update(self, request, pk=None, partial=False):
        if 'material_items' in request.data:
            material_items = request.data['material_items']
            for new_item in material_items:
                if not Material.objects.filter(name__exact=new_item).exists():
                    new_material = Material.objects.create(name=new_item)
                    new_material.save()

        return super().update(request, pk, partial=partial)


class MessageViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('created_at')
    serializer_class = MessageSerializer


class LikeViewSet(LoggingMixin, mixins.CreateModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class HighscoreView(LoggingMixin, mixins.ListModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Event.objects.values('created_by').distinct()
    serializer_class = HighscoreSerializer


class StatisticView(LoggingMixin, mixins.ListModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Event.objects.values(
        month=ExtractMonth('created_at')).annotate(
            year=ExtractYear('created_at')).values(
                'month', 'year').distinct().order_by(
                    'year', 'month')
    serializer_class = StatisticSerializer


class TopViewsView(viewsets.ViewSet):
    queryset = Event.objects.all()

    def list(self, data):
        serializer = TopViewsSerializer(self.queryset, many=True)
        serializer_data = sorted(
            serializer.data, key=lambda k: k['view_count'], reverse=True)[:10]

        return Response(serializer_data)


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


class MaterialItemViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = MaterialItem.objects.all()
    serializer_class = MaterialItemSerializer


class MaterialUnitViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = MaterialUnit.objects.all()
    serializer_class = MaterialUnitSerializer


class MaterialNameViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = MaterialName.objects.all()
    serializer_class = MaterialNameSerializer


class MessageTypeViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = MessageType.objects.all()
    serializer_class = MessageTypeSerializer


class ExperimentViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer


class ExperimentOverviewViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentOverviewSerializer


class FaqViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqRatingViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = FaqRating.objects.all()
    serializer_class = FaqRatingSerializer


class ExperimentItemViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = ExperimentItem.objects.all()
    serializer_class = ExperimentItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = ExperimentItemSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            event = data['event']
            score = data['score']
            if (score == 0):
                total_ratings = ExperimentItem.objects.filter(
                    event=event).count()
                unclear_ratings = ExperimentItem.objects.filter(
                    event=event).filter(
                        score=0).count()
                if (total_ratings >= 1):
                    unclear_rate = unclear_ratings / total_ratings
                    if (unclear_rate >= 0.3):
                        event = Event.objects.filter(id=event)
                        event.update(is_active=False)
                        Event.objects.get(id=event).tags.add(
                            Tag.objects.get(id=70))

        return super().create(request, *args, **kwargs)


class RandomEventViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_active=True).order_by("?")[:10]
    serializer_class = EventSerializer


class AdminEventViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventAdminSerializer


class EventTimestampViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventTimestampSerializer


class ChangePublishStatus(APIView):
    def post(self, request, *args, **kwargs):
        posted_data = self.request.data
        set_active = posted_data['set_active']
        event_id = posted_data['event']

        event = Event.objects.filter(id=event_id)
        event.update(is_active=set_active)

        return_data = [
            {"worked": True}
        ]
        return Response(status=200, data=return_data)


class NextBestHeimabendViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = NextBestHeimabend.objects.order_by("score").all()
    serializer_class = NextBestHeimabendSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('event',)
