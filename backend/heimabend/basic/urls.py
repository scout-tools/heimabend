# myapi/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tag', views.TagViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'message-type', views.MessageTypeViewSet)
router.register(r'like', views.LikeViewSet)
router.register(r'highscore', views.HighscoreView)
router.register(r'tag-category', views.TagCategoryViewSet)
router.register(r'statistic', views.StatisticView)
router.register(r'material-item', views.MaterialItemViewSet)
router.register(r'material-unit', views.MaterialUnitViewSet)
router.register(r'material-name', views.MaterialNameViewSet)
router.register(r'experiment', views.ExperimentViewSet)
router.register(r'experiment-overview', views.ExperimentOverviewViewSet)
router.register(r'experiment-item', views.ExperimentItemViewSet)
router.register(r'random-event', views.RandomEventViewSet)
router.register(r'top-views', views.TopViewsView)
router.register(r'admin-event', views.AdminEventViewSet)
router.register(r'event-timestamp', views.EventTimestampViewSet)
router.register(r'faq-rating', views.FaqRatingViewSet)
router.register(r'faq', views.FaqViewSet)
router.register(r'next-best-heimabend', views.NextBestHeimabendViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('basic/', include(router.urls)),
    url(r'^upload/$', views.ImageView.as_view({'get': 'list'}), name='file-upload'),
    url(r'^event-publish/$', views.ChangePublishStatus.as_view(), name='event-publish')
]
