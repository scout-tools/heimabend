# Generated by Django 3.2 on 2021-04-30 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20210430_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetype',
            name='sorting',
            field=models.IntegerField(auto_created=True, null=True, unique=True),
        ),
    ]
