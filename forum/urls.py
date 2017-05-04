from django.conf.urls import url

from forum.views import ForumSummaryView, TopicTreeListView

urlpatterns = [
    url(r'^$', ForumSummaryView.as_view(), name='forum-summary'),
    url(r'^tree/$',  TopicTreeListView.as_view(), name='forum-tree')
]