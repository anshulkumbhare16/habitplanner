# Generated by Django 5.0.6 on 2024-06-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_app', '0003_topic_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
