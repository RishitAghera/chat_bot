from django.contrib import admin
from django.urls import path, include

from .views import HomePage

urlpatterns = [
    path('home/', HomePage.as_view(),name='home')
]