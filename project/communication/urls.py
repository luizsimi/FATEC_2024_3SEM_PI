from django.urls import path
from .views import video_call

app_name = 'videochamadas'

urlpatterns = [
        path('video_call/', video_call, name='video_call'),
]