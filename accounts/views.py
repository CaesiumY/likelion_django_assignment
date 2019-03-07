from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('blog:home')
        else:
            return render(request, 'login.html', {'error': '이름 또는 비밀번호가 잘못되었습니다.'})
    return render(request, 'login.html',  {'error': '인증방식이 잘못되었습니다.'})


def signup_view(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': '이미 존재하는 계정 이름입니다.'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('blog:home')
        else:
            return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'signup.html')


def logout_view(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog:home')
    return render(request, 'signup.html')
