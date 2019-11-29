# Generated by Django 2.2.7 on 2019-11-29 11:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_event_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='possibleOutside',
            field=models.BooleanField(),
        ),
        migrations.RemoveField(
            model_name='event',
            name='tag',
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.ManyToManyField(default='', to='basic.Tag'),
        ),
    ]
