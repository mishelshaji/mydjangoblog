from administrator.models import Post
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
import markdown

# Create your views here.
def home(request):
    context = {}
    context['posts'] = Post.objects.all().select_related('author').order_by('-created_on')[:20]
    return render(request, 'user/index.html', context)

def about(request):
    return render(request, 'user/about.html')

def view_post(request, url):
    p = get_object_or_404(Post, url=url)
    p.body = markdown.markdown(p.body)
    return render(request, 'user/view_post.html', {'data': p})

def search_post(request):
    search = request.GET.get('q')
    if search is None:
        return redirect('homepage')
    context = {}
    context['posts'] = Post.objects.filter(title__contains=search).select_related('author').order_by('-created_on')[:20]
    return render(request, 'user/index.html', context)