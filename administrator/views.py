from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView
from .models import *
from .forms import PostForm

# Create your views here.
@login_required
def home(request):
    data = Post.objects.filter(author=request.user)
    return render(request, 'administrator/home.html', {'data': data})

@login_required
def create_post(request):
    if request.method == "GET":
        context = {}
        context['form'] = PostForm()
        return render(request, 'administrator/create_post.html', context)
    
    elif request.method == "POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.author = request.user
            p.save()
            messages.success(request, 'New post saved')
            return redirect('admin_home')
        else:
            return render(request, 'administrator/create_post.html', {'form': form})

def delete_post(request, id):
    p = get_object_or_404(Post, id=id, author=request.user)
    p.delete()
    return redirect('admin_home')

def edit_post(request, id):
    p = get_object_or_404(Post, id=id, author=request.user)
    
    if request.method == "GET":
        form = PostForm(instance=p)
        return render(request, 'administrator/create_post.html', {'form': form})
    
    form = PostForm(data=request.POST, instance=p, files=request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Post updated")
        return redirect('admin_home')
    return render(request, 'administrator/create_post.html', {'form': form})
