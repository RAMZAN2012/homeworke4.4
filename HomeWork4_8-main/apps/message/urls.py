from django.urls import path
from apps.message.views import index, delete_message, like_message

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:id>/', delete_message, name='delete_message'),
    path('like/<int:message_id>/', like_message, name='like_message')
]