from django.conf.urls import url

from notes.views import NoteListView, NoteDetailView, NoteCreate, NoteUpdate, NoteDelete

urlpatterns = [
    url(r'^$', NoteListView.as_view(), name='note-list'),
    url(r'^(?P<pk>\d+)/$', NoteDetailView.as_view(), name='note-detail'),
    url(r'note/add/$', NoteCreate.as_view(), name='note-add'),
    url(r'note/(?P<pk>[0-9]+)/$', NoteUpdate.as_view(), name='note-update'),
    url(r'note/(?P<pk>[0-9]+)/delete/$', NoteDelete.as_view(), name='note-delete'),
]