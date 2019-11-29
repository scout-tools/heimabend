# views.py
from rest_framework import viewsets

from .serializers import TagSerializer, EventSerializer
from .models import Tag,Event


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('title')
    serializer_class = EventSerializer