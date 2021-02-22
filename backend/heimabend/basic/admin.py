from django.contrib import admin
from .models import Tag, Event, TagCategory, Event


admin.site.register(Event)
admin.site.register(TagCategory)
admin.site.register(Tag)
