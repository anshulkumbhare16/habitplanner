# Generated by Django 5.0.6 on 2024-06-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_app', '0011_remove_task_unit_remove_userdefinedunits_task_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user_defined_unit',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
