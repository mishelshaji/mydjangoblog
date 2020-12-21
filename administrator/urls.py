from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='admin_home'),
    path('post/create/', create_post, name='admin_create_post'),
    path('post/edit/<int:id>/', edit_post, name='admin_edit_post'),
    path('post/delete/<int:id>', delete_post, name='admin_delete_post'),
]
