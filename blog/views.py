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


def detail_view(request, id):
    post = get_object_or_404(Post, pk=id)

    return render(request, 'detail.html', {'post': post})


def new_view(request):
    return render(request, 'new.html')
