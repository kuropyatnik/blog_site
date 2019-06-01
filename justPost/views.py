from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm, PostForm
from .models import Profile, Posts
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.about_me = form.cleaned_data.get('about_me')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print('User not found')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('login')


def indexView(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = PostForm()

            posts = paginateRecords(request,
                                    Posts.objects.filter(author_id__exact=request.user.id).order_by('-pub_date'))

            return render(request, 'home.html', {'form': form, 'posts': posts})
        elif request.method == 'POST':
            form = PostForm(data=request.POST)
            if form.is_valid():
                author = User.objects.get(id=request.user.id).profile
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                pub_date = datetime.now()
                newPost = Posts(author=author, title=title, content=content, pub_date=pub_date)
                newPost.save()
            return redirect('home')
        return render(request, 'home.html')
    else:
        return redirect('login')


def allPostsView(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            posts = Posts.objects.filter().order_by('-pub_date')
            posts = paginateRecords(request, posts)
            return render(request, 'posts.html', {'posts': posts})
    else:
        return redirect('login')

def authorPostsView(request,stub):
    if request.user.is_authenticated:
        if request.method == 'GET':
            posts = Posts.objects.filter(author__user__username__exact=stub).order_by('-pub_date')
            author = User.objects.filter(username__exact=stub).first()
            posts = paginateRecords(request, posts)
            return render(request, 'author.html',
                          {'posts': posts, 'author_name': author.username, 'about_author': author.profile.about_me})
    else:
        return redirect('login')


def paginateRecords(request, records, num_records=2):
    page = request.GET.get('page', 1)
    paginator = Paginator(records, num_records)
    try:
        records_paginated = paginator.page(page)
    except PageNotAnInteger:
        records_paginated = paginator.page(1)
    except EmptyPage:
        records_paginated = paginator.page(paginator.num_pages)

    return records_paginated
