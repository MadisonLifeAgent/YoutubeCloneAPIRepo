# Generated by Django 3.2.6 on 2021-08-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='videoId',
            field=models.CharField(default=0, max_length=11),
        ),
    ]
