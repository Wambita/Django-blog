from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in immediately after signup
            messages.success(request, 'Account created successfully!')
            return redirect('post_list')  # Redirect to your homepage or another appropriate page
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.info(request, f"You are now logged in as {user.username}")
            return redirect('post_list')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post-detail', pk=post.pk)  # Redirect to the newly created post
        else:
            messages.error(request, 'There was an error creating your post. Please check the form.')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'New Post'})