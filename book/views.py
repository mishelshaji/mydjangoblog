from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'data': books})

def create(request):
    if request.method == "GET":
        bcf = BookCreationForm()
        return render(request, 'book/create.html', {'form': bcf})
    
    bcf = BookCreationForm(request.POST)
    if bcf.is_valid():
        bcf.save()
        return redirect('book_home')
    return render(request, 'book/create.html', {'form': bcf})

def update(request, id):
    book = Book.objects.get(pk=id)
    if request.method == "GET":
        bcf = BookCreationForm(instance=book)
        return render(request, 'book/create.html', {'form': bcf})
    
    bcf = BookCreationForm(data=request.POST, instance=book)
    if bcf.is_valid():
        bcf.save()
        return redirect('book_home')
    return render(request, 'book/create.html', {'form': bcf})

def test(request):
    pass 