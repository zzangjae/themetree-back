# Generated by Django 3.2.12 on 2023-05-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20230518_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='backdrop_path',
            field=models.TextField(null=True),
        ),
    ]