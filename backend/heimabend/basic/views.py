# views.py
from rest_framework import pagination, viewsets, mixins, generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_tracking.mixins import LoggingMixin
from .serializers import TagSerializer, EventSerializer, MessageSerializer, LikeSerializer, HighscoreSerializer, \
    TagCategorySerializer, StatisticSerializer
from .models import Tag, Event, Message, Like, TagCategory
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, BooleanFilter, OrderingFilter, ModelMultipleChoiceFilter, NumberFilter
from django.db.models.functions import ExtractWeek, ExtractYear


class TagViewSet(LoggingMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('is_visible',)


class TagCategoryViewSet(LoggingMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = TagCategory.objects.all()
    serializer_class = TagCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('is_visible',)


class EventPagination(pagination.PageNumberPagination):
    page_size = 3  # the no. of company objects you want to send in one go


class EventFilter(FilterSet):
    isPossibleInside = BooleanFilter(field_name='isPossibleInside')
    isPossibleOutside = BooleanFilter(field_name='isPossibleOutside')
    isPossibleDigital = BooleanFilter(field_name='isPossibleDigital')
    isPossibleAlone = BooleanFilter(field_name='isPossibleAlone')
    isPrepairationNeeded = BooleanFilter(field_name='isPrepairationNeeded')
    isActive = BooleanFilter(field_name='isActive', method='get_isActive')
    withoutCosts = BooleanFilter(method='get_CostRating', field_name='costsRating')
    sorter = OrderingFilter(fields=(
        ('-createdAt', 'newest'),
        ('?', 'random'),
        ('title', 'alpha'),
        ('-like_score', 'rating'),
    ))

    filterTags = ModelMultipleChoiceFilter(field_name='tags__id',
                                           to_field_name='id',
                                           queryset=Tag.objects.all(),
                                           lookup_expr='exact', )
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
                  'sorter',
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
                queryset.filter(isActive=value)
        return queryset.filter(isActive=True)


class EventViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = EventFilter
    ordering = ['-createdAt']
    search_fields = ['title', 'description', 'material']
    pagination_class = EventPagination

    def get_queryset(self):
        print(self.request.user)
        if not self.request.user.is_authenticated:
            return self.queryset.filter(isActive=True).order_by('-createdAt')


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
