# Generated by Django 5.0.6 on 2024-06-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_app', '0002_alter_topic_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
    ]
