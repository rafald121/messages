from django.contrib import admin

# Register your models here.
from messanger.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['content', 'views_count']

admin.site.register(Message, MessageAdmin)
