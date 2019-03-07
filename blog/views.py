from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post

# Create your views here.


def home_view(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 8)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)

    return render(request, 'home.html', {'page_posts': page_posts})
