from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel

class Topic(MPTTModel, TimeStampedModel, TitleSlugDescriptionModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True);
    is_public = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_users = models.ManyToManyField(User, related_name="topics")

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title
