# Generated by Django 5.0.6 on 2024-06-18 14:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_app', '0009_units'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Units',
            new_name='UserDefinedUnits',
        ),
        migrations.AlterField(
            model_name='task',
            name='unit',
            field=models.CharField(max_length=10),
        ),
    ]