# Generated by Django 3.2 on 2021-05-10 08:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_update_field_names_user_types'),
    ]

    operations = [
        migrations.RenameField(model_name='dates_of_class', old_name='id', new_name='date_class_id')
    ]