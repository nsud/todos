# Generated by Django 2.2.10 on 2020-09-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200917_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='todos_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
