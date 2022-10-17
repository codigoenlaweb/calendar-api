from django.contrib import admin
from modules.events.models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    '''Admin View for Event'''

    list_display = ('title', 'note', 'start', 'end', 'user',)
    search_fields = ('title', 'user', 'start', 'end')
    ordering = ('-id',)