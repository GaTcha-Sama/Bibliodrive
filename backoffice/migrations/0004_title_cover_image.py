# Generated by Django 5.1.2 on 2024-11-25 14:26

import backoffice.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_delete_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to=backoffice.models.cover_image_upload_to),
        ),
    ]
