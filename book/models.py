from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
class Book(models.Model):
    CATEGORY = (
        ('science', 'Science'),
        ('tech', 'Technology'),
        ('sports', 'Sports'),
        ('ent', 'Entertainment'),
    )
    
    id = models.BigAutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Book Name',
        validators=[
            MinLengthValidator(5, "Name is too short")
        ]
    )

    description = models.TextField(
        verbose_name='Description',
        blank=True,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(500)
        ]
    )

    author = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Author'
    )

    price = models.IntegerField(
        default=0,
        verbose_name="Price"
    )

    published_on = models.DateField(
        null=False,
        blank=False,
        verbose_name='Published on'
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY,
        verbose_name='Category'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )