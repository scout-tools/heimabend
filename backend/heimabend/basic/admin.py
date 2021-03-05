from django.contrib import admin
from .models import Tag, Event, TagCategory, Event, Image

from django.contrib import admin

admin.site.register(Event)
admin.site.register(TagCategory)
admin.site.register(Tag)
admin.site.register(Image)
