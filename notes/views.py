from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import DetailView

from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from notes.models import Note

class NoteDetailView(DetailView):
    model = Note

class NoteListView(ListView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        return context

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body', 'importance', 'topic']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NoteCreate, self).form_valid(form)

class NoteUpdate(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'body', 'importance', 'topic']
    success_url = reverse_lazy('forum-tree')

    def test_func(self):
        return (self.request.user == self.get_object().created_by)

class NoteDelete(UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('forum-tree')

    def test_func(self):
        return (self.request.user.is_superuser) or (self.request.user == self.get_object().created_by)
    