# Generated by Django 2.2.10 on 2020-09-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_category_todos_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prioritycount',
            name='name',
            field=models.CharField(blank=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]
