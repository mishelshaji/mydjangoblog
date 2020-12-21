from django.db import models
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Category',
    )

    description = models.CharField(
        max_length=255,
        verbose_name='Description'
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created On'
    )

    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated On'
    )

    def __str__(self):
        return self.name

class Post(models.Model):

    class Meta:
        db_table = 'post'

    id = models.BigAutoField(
        primary_key=True
    )

    title = models.CharField(
        max_length=140,
        verbose_name='Title',
        validators=[
            validators.MinLengthValidator(5, "Title is too short"),
            validators.MaxLengthValidator(140, "Title is too long")
        ]
    )

    featured_image = models.ImageField(
        verbose_name='Featured Image',
        upload_to = 'images/',
        blank=True
    )

    description = models.CharField(
        max_length=255,
        verbose_name='Description'
    )

    body = models.TextField(
        verbose_name='Post Content'
    )

    url = models.CharField(
        max_length=250,
        verbose_name='Post URL'
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created On'
    )

    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated On'
    )