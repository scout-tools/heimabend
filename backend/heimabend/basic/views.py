# views.py
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_tracking.mixins import LoggingMixin
from .serializers import TagSerializer, EventSerializer, MessageSerializer, LikeSerializer, HighscoreSerializer
from .models import Tag, Event, Message, Like


class TagViewSet(LoggingMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer


class EventViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('title')
    serializer_class = EventSerializer


class MessageViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('createdAt')
    serializer_class = MessageSerializer


class LikeViewSet(LoggingMixin, mixins.CreateModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class HighscoreView(LoggingMixin, mixins.ListModelMixin, viewsets.ViewSetMixin, generics.GenericAPIView):
    queryset = Event.objects.values('createdBy').distinct()
    serializer_class = HighscoreSerializer
