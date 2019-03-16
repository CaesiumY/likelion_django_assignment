from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.models import User
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
    if request.method == 'POST':
        post = Post()
        post.author = request.user
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.created_at = timezone.datetime.now()
        # post.updated_at = timezone.datetime.now()
        post.save()
        return redirect('/blog/detail/'+str(post.id))
    return render(request, 'new.html')


def delete_view(request, id):
    post = Post.objects.get(pk=id)
    if post.author == request.user:
        post.delete()
        return redirect('/blog/')
    return render(request, 'detail.html', {'post': post, 'error': '본인 글만 삭제할 수 있습니다.'})
