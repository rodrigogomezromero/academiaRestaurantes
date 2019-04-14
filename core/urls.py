from django.urls import path, include

from .views import *
urlpatterns = [
    path('',Test.as_view(),name='test')
]