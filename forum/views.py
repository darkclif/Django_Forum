from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from topics.models import Topic
from notes.models import IMPORTANCE, Note

class ForumSummaryView(TemplateView):
    template_name = "forum_summary.html"

    def get_context_data(self, **kwargs):
        context = super(ForumSummaryView, self).get_context_data(**kwargs)

        context['notes'] = Note.objects.all()

        # Indicator
        if Note.objects.count() > 0:
            indicator = ( (float)( Note.objects.filter(importance=1).count() * 1 + Note.objects.filter(importance=2).count() * 2) / (float)(Note.objects.count() * 2) ) * 100.0
        else:
            indicator = 0

        context['distress_indicator'] = "{:.2f}".format(indicator)

        # Notes summary
        context['notes_green_count'] = Note.objects.filter(importance=0).count()
        context['notes_yellow_count'] = Note.objects.filter(importance=1).count()
        context['notes_red_count'] = Note.objects.filter(importance=2).count()

        # # Topics summary
        # context['topics_green_count'] = Topic.objects.filter(importance=0).count()
        # context['topics_yellow_count'] = Note.objects.filter(importance=1).count()
        # context['topics_red_count'] = Note.objects.filter(importance=2).count()

        return context        

class TopicTreeListView(ListView):
    template_name="forum_list.html"
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicTreeListView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
        return context
