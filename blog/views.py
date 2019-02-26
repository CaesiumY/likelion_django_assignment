from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post

# Create your views here.


def home_view(request):
    return render(request, 'home.html')
