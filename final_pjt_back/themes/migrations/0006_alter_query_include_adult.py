# Generated by Django 3.2.12 on 2023-05-19 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0005_query_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='include_adult',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
