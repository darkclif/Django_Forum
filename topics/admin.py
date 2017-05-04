from django.contrib import admin

from topics.models import Topic

from django_mptt_admin.admin import DjangoMpttAdmin

@admin.register(Topic)
class TopicAdmin(DjangoMpttAdmin):
    list_display=['title', 'is_public']
    list_editable=['is_public']