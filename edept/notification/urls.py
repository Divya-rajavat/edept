from .views import my_notification_view
from django.urls import path

urlpatterns = [
    path('send/', my_notification_view, name='send-notification'),
]