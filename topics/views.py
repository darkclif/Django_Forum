from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from notes.models import Note
from topics.models import Topic
from django.contrib.auth.models import User

class TopicListView(ListView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
        return context

class TopicDetailView(DetailView):
    model = Topic
    
    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(topic=self.get_object().pk)
        context['assigned_users'] = User.objects.filter(topics=self.get_object().pk)
        return context

class TopicCreate(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'parent', 'is_public', 'assigned_users']
    success_url = reverse_lazy('topic-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TopicCreate, self).form_valid(form)

class TopicUpdate(UserPassesTestMixin, UpdateView):
    model = Topic
    fields = ['title', 'parent', 'is_public', 'assigned_users']
    success_url = reverse_lazy('topic-list')

    def test_func(self):
        return self.request.user == self.get_object().created_by

class TopicDelete(UserPassesTestMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy('topic-list')

    def get_context_data(self, **kwargs):
        context = super(TopicDelete, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(topic=self.get_object().pk)
        return context

    def test_func(self):
        return (self.request.user.is_superuser) or (self.request.user == self.object.created_by)
