# Generated by Django 3.2.12 on 2023-05-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0010_auto_20230523_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerquery',
            name='sort_by',
        ),
        migrations.RemoveField(
            model_name='answerquery',
            name='with_crew',
        ),
        migrations.AlterField(
            model_name='answerquery',
            name='include_adult',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answerquery',
            name='language',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answerquery',
            name='release_date_gte',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answerquery',
            name='release_date_lte',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answerquery',
            name='release_year',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answerquery',
            name='vote_average_gte',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answerquery',
            name='vote_average_lte',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answerquery',
            name='with_runtime_gte',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answerquery',
            name='with_runtime_lte',
            field=models.TextField(null=True),
        ),
    ]
