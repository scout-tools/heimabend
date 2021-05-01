# Generated by Django 3.2 on 2021-04-30 15:44

import basic.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_materialname_unit_detaults'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='sorting',
            field=models.IntegerField(auto_created=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=stdimage.models.JPEGField(blank=True, upload_to=basic.models.nameFile),
        ),
    ]
