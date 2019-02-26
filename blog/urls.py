from django.contrib import admin
from django.urls import path, include
from .views import home_view

app_name = 'blog'

urlpatterns = [
    path('', home_view, name='home'),
]
