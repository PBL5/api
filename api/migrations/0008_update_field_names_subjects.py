# Generated by Django 3.2 on 2021-05-10 09:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_update_field_names_dates_class'),
    ]

    operations = [
       migrations.RenameField(model_name='subjects', old_name='id', new_name='subject_id')
    ]
