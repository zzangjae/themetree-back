# Generated by Django 3.2.12 on 2023-05-18 07:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_comment_user_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_likes',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_likes',
            field=models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_hates',
            field=models.ManyToManyField(related_name='hate_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_likes',
            field=models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_viewd',
            field=models.ManyToManyField(related_name='viewed_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
