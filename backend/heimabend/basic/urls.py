# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tag', views.TagViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'like', views.LikeViewSet)
router.register(r'highscore', views.HighscoreView)
router.register(r'tag-category', views.TagCategoryViewSet)
router.register(r'statistic', views.StatisticView)
router.register(r'imageupload', views.ImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('basic/', include(router.urls)),
]
