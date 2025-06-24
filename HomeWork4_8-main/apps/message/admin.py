from django.contrib import admin
from apps.message.models import Message

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'created_at', 'likes')