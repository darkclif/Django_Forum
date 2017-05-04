from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel

from topics.models import Topic

IMPORTANCE = (
    (0, 'Good'),
    (1, 'Warning'),
    (2, 'Bad'),
)

class Note(TimeStampedModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    importance = models.IntegerField(choices=IMPORTANCE)

    def get_importance_color(self):
        switcher = {
            0: "#dff0d8",
            1: "#fcf8e3",
            2: "#f2dede",
        }
        return switcher.get(self.importance, "white")

    def get_importance_class(self):
        switcher = {
            0: "success",
            1: "warning",
            2: "danger",
        }
        return switcher.get(self.importance, "nothing")

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})