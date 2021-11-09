from django import urls
from django.conf.urls import url
from django.urls import path
from .views import TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
]