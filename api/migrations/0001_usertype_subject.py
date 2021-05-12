# Generated by Django 3.1.7 on 2021-04-27 13:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_type',
            fields=[
                ('id', models.AutoField(primary_key=True,
                 null=False, editable=False, unique=True)),
                ('user_type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[('id', models.AutoField(primary_key=True, null=False, editable=False, unique=True)),
                    ('subject_name', models.CharField(max_length=50)),
                    ],
        ),
    ]
