from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('detail/<int:id>/', views.detail_view, name='detail'),
    path('new/', views.new_view, name='new'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
    path('edit/<int:id>/', views.edit_view, name='edit'),
]
