from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from notes.models import Note

admin.site.register(Note)
