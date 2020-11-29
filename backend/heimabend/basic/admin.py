from django.contrib import admin
from .models import Tag, Event, TagCategory, Message, Like

admin.site.register(Event)
admin.site.register(TagCategory)
admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Like)
