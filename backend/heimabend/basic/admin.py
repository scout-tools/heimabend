from django.contrib import admin
from .models import Tag, Event, TagCategory, Event, Image, \
    Material, ExperimentItem, Experiment

from django.contrib import admin

admin.site.register(Event)
admin.site.register(TagCategory)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Material)
admin.site.register(Experiment)
admin.site.register(ExperimentItem)
