# Generated by Django 3.2 on 2021-04-30 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialname',
            name='unit_detaults',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='basic.materialunit'),
        ),
    ]
