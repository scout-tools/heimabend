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
            return self.queryset.filter(is_public=True)
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
            return self.queryset.filter(is_public=True)
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
    is_public = BooleanFilter(field_name='is_public', method='get_is_public')
    withoutCosts = BooleanFilter(
        method='get_cost_rating', field_name='costs_rating')
    filterTags = ModelMultipleChoiceFilter(field_name='tags__id',
                                           to_field_name='id',
                                           queryset=Tag.objects.all(),
                                           method='get_tags')

    class Meta:
        model = Event
        fields = ['prepairation_time',
                  'is_public',
                  'withoutCosts',
                  'filterTags',
                  ]

    def get_CostRating(self, queryset, field_name, value):
        if value:
            return queryset.filter(costs_rating=0)
        return queryset

    def get_is_public(self, queryset, field_name, value):
        if not value:
            if self.request.user.is_authenticated:
                return queryset.filter(is_public=value)
        return queryset.filter(is_public=True)

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
    search_fields = ['title', 'description']
    pagination_class = EventPagination

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.queryset.filter(is_public=True)
        else:
            return self.queryset


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
                        event.update(is_public=False)
                        Event.objects.get(id=event).tags.add(
                            Tag.objects.get(id=70))

        return super().create(request, *args, **kwargs)


class RandomEventViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_public=True).order_by("?")[:10]
    serializer_class = EventSerializer


class AdminEventViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventAdminSerializer


class EventTimestampViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_public=True)
    serializer_class = EventTimestampSerializer


class ChangePublishStatus(APIView):
    def post(self, request, *args, **kwargs):
        posted_data = self.request.data
        set_active = posted_data['set_active']
        event_id = posted_data['event']

        event = Event.objects.filter(id=event_id)
        event.update(is_public=set_active)

        return_data = [
            {"worked": True}
        ]
        return Response(status=200, data=return_data)


class NextBestHeimabendViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = NextBestHeimabend.objects.order_by("score").all()
    serializer_class = NextBestHeimabendSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('event',)


class MaterialItems(APIView):
    def post(self, request, *args, **kwargs):
        posted_data = self.request.data
        return_array = []
        for item in posted_data:

            material_name_count = MaterialName.objects.filter(
                name=item['name']
            ).count()

            if (material_name_count == 0):
                material_name_new = MaterialName.objects.create(
                    name=item['name']
                )
                material_name_new.save()

            material_name_obj = MaterialName.objects.filter(
                name=item['name']
            ).first()

            if (item['id'] > 0):
                material_item = MaterialItem.objects.filter(
                    id=item['id']
                )

                material_item.update(
                    quantity=item['quantity'],
                    material_name_id=material_name_obj.id,
                    material_unit_id=item['unit_id']
                )
                return_array.append(item['id'])
            else:
                new_obj = MaterialItem.objects.create(
                    quantity=item['quantity'],
                    material_name_id=material_name_obj.id,
                    material_unit_id=item['unit_id']
                )
                new_obj.save()

                return_array.append(new_obj.id)

        return_data = [
            {"material_event_ids": return_array}
        ]
        return Response(status=200, data=return_data)
