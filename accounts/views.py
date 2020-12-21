import django
from book.forms import BookCreationForm
from book.models import Book
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def user_login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {"form": AuthenticationForm()})
    else:
        lf = AuthenticationForm(data=request.POST)
        if lf.is_valid():
            username = lf.cleaned_data.get('username')
            password = lf.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                target = request.GET.get('next')
                if target:
                    return redirect(target)
                return redirect('admin_home')
        return render(request, 'accounts/login.html', {"form": lf})


def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html', {"form": UserCreationForm()})

def user_logout(request):
    logout(request)
    return redirect('homepage')