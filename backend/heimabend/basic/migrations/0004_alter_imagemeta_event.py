# Generated by Django 3.2 on 2021-05-09 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20210507_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemeta',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_id', to='basic.event'),
        ),
    ]
