from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='book_home'),
    path('create/', create, name='book_create'),
    path('update/<int:id>/', update, name='book_upadate'),
    path('test/', test, name='book_test'),
]