# views.py
from rest_framework import pagination, viewsets, mixins, generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_tracking.mixins import LoggingMixin
from .serializers import TagSerializer, EventSerializer, MessageSerializer, LikeSerializer, HighscoreSerializer
from .models import Tag, Event, Message, Like
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, BooleanFilter, OrderingFilter, ModelMultipleChoiceFilter, NumberFilter


class TagViewSet(LoggingMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer


class EventPagination(pagination.PageNumberPagination):
    page_size = 5  # the no. of company objects you want to send in one go


class EventFilter(FilterSet):
    isPossibleDigital = BooleanFilter(field_name='isPossibleDigital')
    isPossibleAlone = BooleanFilter(field_name='isPossibleAlone')
    isPrepairationNeeded = BooleanFilter(field_name='isPrepairationNeeded')
    isActive = BooleanFilter(field_name='isActive')
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
        fields = [  # 'isPossibleInside',
            # 'isPossibleOutside',
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


class EventViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = EventPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = EventFilter
    search_fields = ['title', 'description', 'material']


class MessageViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('createdAt')
    serializer_class = MessageSerializer


class LikeViewSet(LoggingMixin, mixins.CreateModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class HighscoreView(LoggingMixin, mixins.ListModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Event.objects.values('createdBy').distinct()
    serializer_class = HighscoreSerializer
